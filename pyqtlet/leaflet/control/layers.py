from .control import Control

class Layers(Control):

    @property
    def controlName(self):
        return self._jsName

    @property
    def jsName(self):
        return self._jsName

    def __init__(self, layers=None, overlays=None, options=None):
        super().__init__()
        self.layers = layers
        self.overlays = overlays
        self.options = options
        self._jsName = 'controlLayers'
        self._initJs()

    def _initJs(self):
        jsObject = 'L.control.layers({layers}'.format(layers=self.layers)
        if self.overlays:
            jsObject += ', {overlays}'.format(overlays=self.overlays)
        if self.options:
            jsObject += ', {options}'.format(options=self.options)
        jsObject += ')'
        self._createJsObject(jsObject)

