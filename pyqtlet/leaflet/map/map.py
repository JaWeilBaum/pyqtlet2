import json
import os
import time

from PyQt5.QtCore import QObject, QEventLoop, pyqtSignal, pyqtSlot

from ... import mapwidget

class Map(QObject):
    """
    L.map equivalent in PyQtlet
    """
    jsComplete = pyqtSignal()

    @property
    def mapWidget(self):
        return self._mapWidget

    @mapWidget.setter
    def mapWidget(self, mapWidget):
        if not issubclass(type(mapWidget), mapwidget.MapWidget):
            raise TypeError(('Expected mapWidget of type pyqtlet.MapWidget, '
                            'received {type_}'.format(type_=type(mapWidget))))
        self._mapWidget = mapWidget
        
    def __init__(self, mapWidget):
        super().__init__()
        self.mapWidget = mapWidget
        self.layers = []

    def setView(self, latLng, zoom='', options=''):
        js = 'map.setView({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        print(js)
        self.mapWidget.page.runJavaScript(js)

    def addOSMBaseMap(self):
        osm = """L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map)"""
        self.mapWidget.page.runJavaScript(osm)

    def addLayer(self, layer):
        jsObject = layer.leafletJsObject
        js = 'map.addLayer({obj});'.format(obj=jsObject)
        print(js)
        self.mapWidget.page.runJavaScript(js)

    def getDrawn(self):
        geo = self._getJsResponse('getDrawn();')
        return json.loads(geo)

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

