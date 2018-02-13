from ..layer import Layer

class Marker(Layer):
    def __init__(self, latLng, options=None):
        super().__init__()
        self.latLng = latLng
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'L.marker({latLng}'.format(latLng=self.latLng)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

    def setLatLng(self, latLng):
        js = '{layerName}.setLatLng({latLng})'.format(
                layerName=self._layerName, latLng=latLng)
        self.runJavaScript(js)

    def setOpacity(self, opacity):
        js = '{layerName}.setOpacity({latLng})'.format(
                layerName=self._layerName, opacity=opacity)
        self.runJavaScript(js)
