import json
import os
import time

from PyQt5.QtCore import pyqtSlot

from ... import mapwidget
from ..core import Evented

class Map(Evented):
    """
    L.map equivalent in PyQtlet
    """

    @property
    def layers(self):
        """
        Instead of L.map.eachLayer
        """
        return self._layers

    def __init__(self, mapWidget, options=None):
        super().__init__(mapWidget)
        self.options = options
        self._layers = []
        self._initJs()

    def _initJs(self):
        js = 'var map = L.map("map"'
        if self.options:
            js += ', {options}'.format(options=self.options)
        js += ')'
        self.runJavaScript(js)
        js = 'var mapObject = null; \
              new QWebChannel(qt.webChannelTransport, function(c) { \
                  mapObject = c.objects.mapObject;\
              });'
        self.runJavaScript(js)
        js = 'map.on("click", function(e){mapObject.printCoords(e.latlng)});'
        self.runJavaScript(js)

    @pyqtSlot(dict)
    def printCoords(self, coords):
        print(coords)

    def setView(self, latLng, zoom=None, options=None):
        js = 'map.setView({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def addLayer(self, layer):
        self._layers.append(layer)
        layer.map = self
        js = 'map.addLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScript(js)

    def removeLayer(self, layer):
        if layer not in self._layers:
            # TODO Should we raise a ValueError here? Or just return
            return
        self._layers.remove(layer)
        layer.map = None
        js = 'map.removeLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScript(js)

    def getBounds(self):
        return self.getJsResponse('map.getBounds()')

    def getCenter(self):
        return self.getJsResponse('map.getCenter()')

    def getZoom(self):
        return self.getJsResponse('map.getZoom()')

    def hasLayer(self, layer):
        return layer in self._layers

    def setZoom(self, zoom, options=None):
        js = 'map.setZoom({zoom}'.format(zoom=zoom);
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def setMaxBounds(self, bounds):
        js = 'map.setMaxBounds({bounds})'.format(bounds=bounds)
        self.runJavaScript(js)

    def setMaxZoom(self, zoom):
        js = 'map.setMaxZoom({zoom})'.format(zoom=zoom)
        self.runJavaScript(js)

    def setMinZoom(self, zoom):
        js = 'map.setMinZoom({zoom})'.format(zoom=zoom)
        self.runJavaScript(js)

    def panTo(self, latLng, options=None):
        js = 'map.panTo({latLng}'.format(latLng=latLng);
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def setView(self, latLng, zoom=None, options=None):
        js = 'map.flyTo({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)
