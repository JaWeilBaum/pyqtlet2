from PyQt5.QtCore import QObject, QEventLoop, pyqtSignal

from ... import mapwidget

class Evented(QObject):
    mapWidget = None
    jsComplete = pyqtSignal()

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

    # This may cause issues if multiple calls are made at the same time
    # since self.response would be shared. I am not sure how to eliminate this.
    def _getJsResponse(self, js):
        loop = QEventLoop()
        self.jsComplete.connect(loop.quit)
        self.mapWidget.page.runJavaScript(js, self._returnJs)
        loop.exec()
        return self.response

    def _returnJs(self, response):
        self.response = response
        self.jsComplete.emit()

