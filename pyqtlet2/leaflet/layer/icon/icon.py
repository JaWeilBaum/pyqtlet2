from ..layer import Layer
from pyqtlet2.leaflet.core.Parser import Parser


class Icon(Layer):
    def __init__(self, iconUrl: str, options=None):
        super().__init__()
        if isinstance(options, type(None)):
            options = {}
        self.iconUrl = iconUrl
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'L.icon({options});'.format(options=Parser.dict_for_js({"iconUrl": self.iconUrl,
                                                                                  **self.options}))
        self._createJsObject(leafletJsObject)