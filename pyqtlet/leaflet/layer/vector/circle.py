from .circlemarker import CircleMarker


class Circle(CircleMarker):
    def __init__(self, latLng, radius, options=None):
        self.radius = radius
        super().__init__(latLng, options)

    def _initJs(self):
        leafletJsObject = 'L.circle({latLng},{radius}'.format(latLng=self.latLng,
                radius=self.radius)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

