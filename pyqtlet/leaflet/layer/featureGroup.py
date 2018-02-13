from .layerGroup import LayerGroup

class FeatureGroup(LayerGroup):
    def __init__(self, layers=None, options=None):
        super().__init__(layers)
        self.layers = layers
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'new L.FeatureGroup('
        if self.layers:
            leafletJsObject+='{l}'.format(l=self.layers)
        if self.layers and self.options:
            leafletJsObject += ','
        if self.options:
            leafletJsObject += '{options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

