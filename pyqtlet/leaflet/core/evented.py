import logging

from PyQt5.QtCore import QObject, QEventLoop, pyqtSignal, pyqtSlot, QThread, QTimer

from ... import mapwidget

class WorkerThread(QThread):
    completed = pyqtSignal()
    def __init__(self, work, js):
        QThread.__init__(self)
        self.work = work
        self.js = js
        self.response = None
        self.completed.connect(lambda: print('completed emit'))

    @pyqtSlot()
    def run(self):
        loop = QEventLoop()
        self.completed.connect(loop.quit)
        loop.exec()
        print('run response', self.response)
        return self.response

    def doWork(self):
        pass

    @pyqtSlot(str)
    def callback(self, response):
        self.response = response
        print('callback function', response)
        self.completed.emit()

class Evented(QObject):
    '''
    Base class for all pyqtlet objects. 
    Handles initiation, as well as all python<->js communication
    '''
    mapWidget = None
    jsComplete = pyqtSignal()

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

    def getJsResponse(self, js):
        # Qt runs runJavaScript function asynchronously. So if we want 
        # to get a response from leaflet, we need to force it to be sync
        # We create a thread that runs the code, waits for the response
        # and then returns the response that was saved in the thread
        # js = f'var response = {js};channelObjects.{self.jsName}Object.jsComplete.emit();channelObjects.{self.jsName}Object._setResponse(JSON.strigify(response));;'
        loop = QEventLoop()
        thread = WorkerThread(self.mapWidget.page.runJavaScript, js)
        thread.start()
        self.mapWidget.page.runJavaScript(js, thread.callback)
        thread.finished.connect(loop.quit)
        loop.exec()
        return thread.response

    @pyqtSlot(str)
    def _setResponse(self, response):
        print('response', response)
        self.response = response

    @pyqtSlot(str)
    def _onJsResponse(self, response):
        print('response', response)
        self.response = response
        self.jsComplete.emit()

    def startScript(self):
        self._logger.debug('getting Js response: {js}'.format(js=self.js))
        self.mapWidget.page.runJavaScript(self.js, self._onJsResponse)

    def runJavaScript(self, js):
        self._logger.debug('Running JS: {js}'.format(js=js))
        self.mapWidget.page.runJavaScript(js)

    def runJavaScriptWithResult(self, js, callback):
        self._logger.debug('Running JS with callback: {js}, {callback}'.format(js=js, callback=callback.__name__))
        self.mapWidget.page.runJavaScript(js, callback)

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

