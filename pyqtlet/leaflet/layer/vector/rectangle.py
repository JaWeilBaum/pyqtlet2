from .polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, bounds, options=None):
        super().__init__()
        self.bounds = bounds
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'L.rectangle({bounds}'.format(bounds=self.bounds)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self.createJsObject(leafletJsObject)

