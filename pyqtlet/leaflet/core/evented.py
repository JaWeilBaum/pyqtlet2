import logging

from PyQt5.QtCore import QObject, QEventLoop, pyqtSignal, pyqtSlot, QThread

from ... import mapwidget


class JsThread(QThread):
    jsComplete = pyqtSignal()
    def __init__(self, page, js=None):
        super().__init__()
        self.page = page
        self.js = js
        self.response = None
        self._logger = logging.getLogger(__name__)

    def _jsResponse(self, response):
        self._logger.debug('jsthread got response: {response}'.format(response=response))
        self.response = response
        self.jsComplete.emit()

    def setJs(self, js):
        self.js = js

    def run(self):
        loop = QEventLoop()
        self._logger.debug('running jsthread: {js}'.format(js=self.js))
        self.jsComplete.connect(loop.quit)
        self.page.runJavaScript(self.js, self._jsResponse)
        loop.exec()


class Evented(QObject):
    '''
    Base class for all pyqtlet objects. 
    Handles initiation, as well as all python<->js communication
    '''
    mapWidget = None
    _jsComplete = pyqtSignal()

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
        self.jsThread = JsThread(self.mapWidget.page,'')
        js = ('var channelObjects = null;'
              'new QWebChannel(qt.webChannelTransport, function(channel) {'
              '    channelObjects = channel.objects;'
              '});')
        self.runJavaScript(js)

    def getJsResponse(self, js):
        # We create a thread that runs the code, waits for the response
        # and then saves it in the thread
        # NOTE: I'm not sure why this doesn't need an eventloop, and how
        # the response comes...
        self.jsThread.setJs(js)
        self.jsThread.start()
        return self.jsThread.response

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

