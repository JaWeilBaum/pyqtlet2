from .layer import Layer

class LayerGroup(Layer):

    @property
    def layers(self):
        return self._layers

    def __init__(self):
        super().__init__()
        self._layers = []

    def _initJs(self):
        leafletJsObject = 'new L.layerGroup()'.format(latLng=self.latLng)
        self.createJsObject(leafletJsObject)

    def addLayer(self, layer):
        self.map.addLayer(layer)
        self._layers.append(layer)

    def removeLayer(self, layer):
        if not layer in self._layers:
            # TODO Raise ValueError?
            return
        self.map.removeLayer(layer)
        self._layers.remove(layer)

