from .polyline import Polyline


class Polygon(Polyline):
    def __init__(self, latLngs, options=None):
        super().__init__()
        self.latLngs = latLngs
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'L.polygon({latLngs}'.format(latLngs=self.latLngs)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self.createJsObject(leafletJsObject)

