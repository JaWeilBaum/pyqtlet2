from ..layer import Layer

class Marker(Layer):
    def __init__(self, latLng, options=None):
        self.latLng = latLng
        self.options = options
        self.leafletJsObject = ''
        self._initJs()

    def _initJs(self):
        self.leafletJsObject = 'L.marker({latLng}'.format(latLng=self.latLng)
        if self.options:
            self.leafletJsObject += ', {options}'.format(options=self.options)
        self.leafletJsObject += ')'
        print(self.leafletJsObject)

