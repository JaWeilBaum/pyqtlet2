import logging
import time

from PyQt5.QtCore import QObject, QJsonValue

from ... import mapwidget


class Evented(QObject):
    '''
    Base class for all pyqtlet2 objects.
    Handles initiation, as well as all python<->js communication
    '''
    mapWidget = None

    def __init__(self, mapWidget=None):
        '''
        Base class for all pyqtlet2 objects
        Handles initiation, as well as python-Js communication
        The first pyqtlet2 object to be initiated should be pyqtlet2.L.map
        This will allow all the pyqtlet2 objects to have access to the
        widget and thus the ability to implement leaflet via python.

        :param pyqtlet2.MapWidget mapWidget: The mapwidget object
            Should only be sent once, when the first object is being 
            initialised.
        '''
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(9)
        self.response = None
        if Evented.mapWidget:
            return
        if mapWidget is None:
            raise RuntimeError('L.map must be initialised before other pyqtlet2 objects')
        if not issubclass(type(mapWidget), mapwidget.MapWidget):
            raise TypeError(('Expected mapWidget of type pyqtlet2.MapWidget, '
                            'received {type_}'.format(type_=type(mapWidget))))
        Evented.mapWidget = mapWidget
        js = ('var channelObjects = null;'
              'new QWebChannel(qt.webChannelTransport, function(channel) {'
              '    channelObjects = channel.objects;'
              '});')
        self.runJavaScript(js)
        self.mapWidget.page.titleChanged.connect(lambda: print('title changed'))

    def getJsResponse(self, js, callback):
        '''
        Runs javascript code in the mapWidget and triggers callback.

        Can be used for custom use cases where information is required
        from the mapwidget, and the existing code does not cover the
        requirement
        
        :param str js: The javascript code
        :param function callback: The function that will consume the 
            javascript response

        .. note:: 
            Qt runs runJavaScript function asynchronously. So if we want 
            to get a response from leaflet, we need to force it to be sync
            In all that I have tried, I was unable to get the response from
            the same function, so I am converting it to a method with callback
        '''
        self._logger.debug('Running JS with callback: {js}=>{callback}'.format(
            js=js, callback=callback.__name__))
        self.mapWidget.page.runJavaScript(js, callback)

    def runJavaScript(self, js):
        '''
        Runs javascript code in the mapWidget.

        Can be used for custom use cases where the existing code,
        methods etc. do not cover the requirements.

        :param str js: The javascript code
        '''
        self._logger.debug('Running JS: {js}'.format(js=js))
        self.mapWidget.page.runJavaScript(js)

    def _createJsObject(self, leafletJsObject):
        '''
        Function to create variables/objects in leaflet in the
        javascript "engine", and registers the object so that it can
        be called in the webchannel.

        :param str leafletJsObject: javascript code that creates the
            leaflet object
        '''
        # Creates the js object on the mapWidget page
        js = 'var {name} = {jsObject}'.format(name=self.jsName, 
                jsObject=leafletJsObject)
        self.runJavaScript(js)
        # register the object in the channel
        self.mapWidget.channel.registerObject(
                '{name}Object'.format(name=self.jsName), self)

    def _connectEventToSignal(self, event, signalEmitter):
        # We need to delete some keys as they are causing circular structures
        js = '{name}.on("{event}", function(e) {{\
                  delete e.target;\
                  delete e.sourceTarget;\
                  e = copyWithoutCircularReferences([e], e);\
                  channelObjects.{name}Object.{signalEmitter}(e)}})'.format(
            name=self.jsName, event=event, signalEmitter=signalEmitter)
        self.runJavaScript(js)

    def _stringifyForJs(self, object_):
        # When passing options to JS, sometimes we need to pass in objects
        # this method and _handleObject take care of that
        # Some arguments are strings and some are objects. We also make sure
        # that the objects are not sent as strings. Similarly, we also convert
        # python bool to js bool etc.
        jsString = str(self._handleObject(object_))
        jsString = jsString.replace('\'__pyqtletObjectStart__', '')
        jsString = jsString.replace('\"__pyqtletObjectStart__', '')
        jsString = jsString.replace('__pyqtletObjectEnd__\'', '')
        jsString = jsString.replace('__pyqtletObjectEnd__\"', '')
        return jsString

    def _handleObject(self, object_):
        if type(object_) is list:
            return [self._handleObject(item) for item in object_]
        if type(object_) is dict:
            return {key: self._handleObject(object_[key]) for key in object_}
        if issubclass(object_.__class__, Evented):
            return '__pyqtletObjectStart__{name}__pyqtletObjectEnd__'.format(name=object_.jsName)
        if object_ is True:
            return '__pyqtletObjectStart__true__pyqtletObjectEnd__'
        if object_ is False:
            return '__pyqtletObjectStart__false__pyqtletObjectEnd__'
        if object_ is None:
            return '__pyqtletObjectStart__null__pyqtletObjectEnd__'
        return object_

    def _qJsonValueToDict(self, object_):
        # Qt returns QJsonValue from within the QChannel. Converting
        # that into a dict is a small recursive function.
        if type(object_) is QJsonValue:
            return self._qJsonValueToDict(self._qJsonToRespectiveType(object_))
        if type(object_) is list:
            return [self._qJsonValueToDict(item) for item in object_]
        if type(object_) is dict:
            return {key: self._qJsonValueToDict(object_[key]) for key in object_}
        return object_

    def _qJsonToRespectiveType(self, object_):
        # A QJsonValue can be one of many types. This function just
        # converts into the correct type
        if object_.isArray():
            return object_.toArray()
        if object_.isBool():
            return object_.toBool()
        if object_.isDouble():
            return object_.toDouble()
        if object_.isNull():
            return None
        if object_.isObject():
            return object_.toObject()
        if object_.isString():
            return object_.toString()
        if object_.isUndefined():
            return None

