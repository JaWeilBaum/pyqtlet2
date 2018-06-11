from .layer import Layer

class LayerGroup(Layer):
    """
    Used to group several layers and handle them as one. If you add it to the map, any layers added or removed from the group will be added/removed on the map as well. 
    """

    @property
    def layers(self):
        return self._layers

    def __init__(self):
        super().__init__()
        self._layers = []
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'new L.layerGroup()'
        self._createJsObject(leafletJsObject)

    def addLayer(self, layer):
        self._layers.append(layer)
        js = '{layerGroup}.addLayer({layerName})'.format(layerGroup=self._layerName,
                layerName=layer._layerName)
        self.runJavaScript(js)

    def removeLayer(self, layer):
        if not layer in self._layers:
            # TODO Raise ValueError?
            return
        self._layers.remove(layer)
        js = '{layerGroup}.removeLayer({layerName})'.format(layerGroup=self._layerName,
                layerName=layer._layerName)
        self.runJavaScript(js)
    
    def clearLayers(self):
        js = '{layerGroup}.clearLayers()'.format(layerGroup=self._layerName)
        self.runJavaScript(js)
    
    def toGeoJSON(self, callback):
        self.getJsResponse('{layer}.toGeoJSON()'.format(layer=self.jsName), callback)

