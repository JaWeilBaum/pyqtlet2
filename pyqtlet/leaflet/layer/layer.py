from ..core import Evented

class Layer(Evented):

    layerId = 0

    @property
    def layerName(self):
        return self._layerName

    @layerName.setter
    def layerName(self, name):
        self._layerName = name

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, map_):
        self._map = map_

    def __init__(self):
        super().__init__()
        self._map = None
        self._layerName = ''

    def getNewLayerName(self):
        layerName = 'l{}'.format(self.layerId)
        Layer.layerId += 1
        return layerName

    def createJsObject(self, leafletJsObject):
        self._layerName = self.getNewLayerName()
        js = '{layerName} = {jsObject}'.format(layerName=self._layerName, 
                jsObject=leafletJsObject)
        self.runJavaScript(js)

    def addTo(self, map_):
        map_.addLayer(self)
