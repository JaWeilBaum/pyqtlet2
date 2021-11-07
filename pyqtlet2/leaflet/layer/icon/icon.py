from ..layer import Layer
from ...core.Parser import Parser
import os


class Icon(Layer):
    def __init__(self, iconUrl: str, options=None):
        super().__init__()
        if isinstance(options, type(None)):
            options = {}
        self.iconUrl = iconUrl
        self.icon_found = False
        self.options = options
        self._check_icon_url()
        self._initJs()

    def _check_icon_url(self):
        if "http" in self.iconUrl:
            self._log.info("Can't check if icon exists at url!")
            return
        if not os.path.isfile(self.iconUrl):
            self._log.error(f"Can't locate file at path: '{self.iconUrl}'. Current working directory is '{os.getcwd()}'")
            return
        self.icon_found = True

    def _initJs(self):
        leafletJsObject = 'L.icon({options});'.format(options=Parser.dict_for_js({"iconUrl": self.iconUrl,
                                                                                  **self.options}))
        self._createJsObject(leafletJsObject)