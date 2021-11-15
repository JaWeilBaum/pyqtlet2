from ..core import Evented
import logging

class Layer(Evented):

    # layerId is a static variable shared between all layers
    # It is used to give unique names to layers
    layerId = 0

    @property
    def layerName(self):
        return self._layerName

    @layerName.setter
    def layerName(self, name):
        self._layerName = name

    @property
    def jsName(self):
        return self._layerName

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, map_):
        self._map = map_

    def __init__(self):
        super().__init__()
        self._map = None
        self._layerName = self._getNewLayerName()
        self._log = logging.getLogger(f"layer_{self._layerName}")

    def _getNewLayerName(self):
        layerName = 'l{}'.format(self.layerId)
        Layer.layerId += 1
        return layerName

    def addTo(self, map_):
        map_.addLayer(self)
        return self

    def removeFrom(self, map_):
        map_.removeLayer(self)
        return self

    def bindPopup(self, content, options=None):
        js = '{layerName}.bindPopup("{content}"'.format(
                layerName=self._layerName, content=content)
        if options:
            js += ', {options}'.format(self._stringifyForJs(options))
        js += ')'
        self.runJavaScript(js)
        return self

    def unbindPopup(self):
        js = '{layerName}.unbindPopup()'.format(layerName=self._layerName)
        self.runJavaScript(js)
        return self

    def bindTooltip(self, content, options=None):
        js = '{layerName}.bindTooltip("{content}"'.format(
                layerName=self._layerName, content=content)
        if options:
            js += ', {options}'.format(self._stringifyForJs(options))
        js += ')'
        self.runJavaScript(js)
        return self

    def unbindTooltip(self):
        js = '{layerName}.unbindTooltip()'.format(layerName=self._layerName)
        self.runJavaScript(js)
        return self


