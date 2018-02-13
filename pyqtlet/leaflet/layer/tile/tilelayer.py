from . import GridLayer

class TileLayer(GridLayer):
    def __init__(self, urlTemplate, options=None):
        super().__init__()
        self.urlTemplate = urlTemplate
        self.options = options
        self._initJs()
        
    def _initJs(self):
        leafletJsObject = 'L.tileLayer("{urlTemplate}"'.format(urlTemplate=self.urlTemplate)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

