import json
import os
import time


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

    def setView(self, latLng, zoom='', options=''):
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

