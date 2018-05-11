import logging
import time

from PyQt5.QtCore import QObject

from ... import mapwidget


class Evented(QObject):
    '''
    Base class for all pyqtlet objects. 
    Handles initiation, as well as all python<->js communication
    '''
    mapWidget = None

    def __init__(self, mapWidget=None):
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self.response = None
        if Evented.mapWidget:
            return
        if mapWidget is None:
            raise RuntimeError('L.map must be initialised before other pyqtlet objects')
        if not issubclass(type(mapWidget), mapwidget.MapWidget):
            raise TypeError(('Expected mapWidget of type pyqtlet.MapWidget, '
                            'received {type_}'.format(type_=type(mapWidget))))
        Evented.mapWidget = mapWidget
        js = ('var channelObjects = null;'
              'new QWebChannel(qt.webChannelTransport, function(channel) {'
              '    channelObjects = channel.objects;'
              '});')
        self.runJavaScript(js)
        self.mapWidget.page.titleChanged.connect(lambda: print('title changed'))

    def getJsResponse(self, js, callback):
        # Qt runs runJavaScript function asynchronously. So if we want 
        # to get a response from leaflet, we need to force it to be sync
        # In all that I have tried, I was unable to get the response from
        # the same function, so I am converting it to a method with callback
        self._logger.debug('Running JS with callback: {js}=>{callback}'.format(
            js=js, callback=callback.__name__))
        self.mapWidget.page.runJavaScript(js, callback)

    def runJavaScript(self, js):
        self._logger.debug('Running JS: {js}'.format(js=js))
        self.mapWidget.page.runJavaScript(js)

    def _createJsObject(self, leafletJsObject):
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
                  channelObjects.{name}Object.{signalEmitter}(e)}})'.format(
            name=self.jsName, event=event, signalEmitter=signalEmitter)
        self.runJavaScript(js)

