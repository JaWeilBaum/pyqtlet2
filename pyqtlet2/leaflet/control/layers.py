from .control import Control

class Layers(Control):

    def __init__(self, layers=[], overlays={}, options=None):
        super().__init__()
        self.layers = layers
        self.overlays = overlays
        self.options = options
        self._initJs()

    def _initJs(self):
        jsObject = 'L.control.layers({layers}'.format(layers=self._stringifyForJs(self.layers))
        if self.overlays is not None:
            jsObject += ', {overlays}'.format(overlays=self._stringifyForJs(self.overlays))
        if self.options is not None:
            jsObject += ', {options}'.format(options=self._stringifyForJs(self.options))
        jsObject += ')'
        self._createJsObject(jsObject)

