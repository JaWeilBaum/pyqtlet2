from .layer import Layer

class imageOverlay(Layer):
    def __init__(self, imageURL, bounds, options=None):
        super().__init__()
        self.imageURL = imageURL
        self.bounds = bounds
        self.options = options
        self._initJs()
        
    def _initJs(self):
        leafletJsObject = 'L.imageOverlay("{imageURL}",{bounds}'.format(imageURL=self.imageURL,bounds=self.bounds)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

