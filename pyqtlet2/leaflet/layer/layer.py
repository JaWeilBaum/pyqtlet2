from ..core import Evented
import logging
from abc import abstractmethod

class Layer(Evented):

    # layerId is a static variable shared between all layers
    # It is used to give unique names to layers
    layerId = 0

    @property
    def layerName(self):
        return self._layerName

    @layerName.setter
    def layerName(self, name):
        self._layerName = name

    @property
    def jsName(self):
        return self._layerName

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, map_):
        self._map = map_

    @abstractmethod
    def _initJs(self):
        raise NotImplemented

    def runJavaScriptForMapIndex(self, js):
        if self._map is not None:
            self.runJavaScript(js, self._map.mapWidgetIndex)

    def __init__(self):
        super().__init__()
        self._map = None
        self._layerName = self._getNewLayerName()
        self._log = logging.getLogger(f"layer_{self._layerName}")
        self._popup = None
        self._popupOptions = None
        self._tooltip = None
        self._tooltipOptions = None

    def _initPopupAndTooltip(self):
        if self._popup is not None:
            self._bindPopupOrTooltip("Popup", self._popup, self._popupOptions)
        if self._tooltip is not None:
            self._bindPopupOrTooltip("Tooltip", self._tooltip, self._tooltipOptions)

    def _bindPopupOrTooltip(self, kind, content, options):
        js = f'{self._layerName}.bind{kind}("{content}"'
        if options is not None:
            js += f', {self._stringifyForJs(options)}'
        js += ')'
        self.runJavaScriptForMapIndex(js)

    def _getNewLayerName(self):
        layerName = 'l{}'.format(self.layerId)
        Layer.layerId += 1
        return layerName

    def addTo(self, map_):
        map_.addLayer(self)
        return self

    def removeFrom(self, map_):
        map_.removeLayer(self)
        return self

    def bindPopup(self, content, options=None):
        self._popup = content
        self._popupOptions = options
        self._bindPopupOrTooltip("Popup", self._popup, self._popupOptions)
        return self

    def unbindPopup(self):
        self._popup = None
        self._popupOptions = None
        js = '{layerName}.unbindPopup()'.format(layerName=self._layerName)
        self.runJavaScriptForMapIndex(js)
        return self

    def bindTooltip(self, content, options=None):
        self._tooltip = content
        self._tooltipOptions = options
        self._bindPopupOrTooltip("Tooltip", self._tooltip, self._tooltipOptions)
        return self

    def unbindTooltip(self):
        self._tooltip = None
        self._tooltipOptions = None
        js = '{layerName}.unbindTooltip()'.format(layerName=self._layerName)
        self.runJavaScriptForMapIndex(js)
        return self


