from PyQt5.QtCore import QObject, QEventLoop, pyqtSignal

from ... import mapwidget

class Evented(QObject):
    '''
    Base class for all pyqtlet objects. 
    Handles initiation, as well as all python<->js communication
    '''
    mapWidget = None
    _jsComplete = pyqtSignal()

    def __init__(self, mapWidget=None):
        super().__init__()
        if Evented.mapWidget:
            return
        if mapWidget is None:
            raise RuntimeError('L.map must be initialised before other pyqtlet objects')
        if not issubclass(type(mapWidget), mapwidget.MapWidget):
            raise TypeError(('Expected mapWidget of type pyqtlet.MapWidget, '
                            'received {type_}'.format(type_=type(mapWidget))))
        Evented.mapWidget = mapWidget

    # TODO
    # This may cause issues if multiple calls are made at the same time
    # since self.response and self._jsComplete would be shared. 
    # I am not sure how to eliminate this.
    def getJsResponse(self, js):
        # We need a loop to force the execution to be sychronous
        # TODO Fix bug if runJavaScript executes before loop.exec begins
        loop = QEventLoop()
        self._jsComplete.connect(loop.quit)
        self.mapWidget.page.runJavaScript(js, self._returnJs)
        loop.exec()
        return self.response

    def _returnJs(self, response):
        self.response = response
        self._jsComplete.emit()

    def runJavaScript(self, js):
        # TODO Do we need loop here as well?
        self.mapWidget.page.runJavaScript(js)

