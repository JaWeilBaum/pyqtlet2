from ..layer import Layer
from ..icon import Icon
from ...core.Parser import Parser
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QJsonValue
from typing import List


class Marker(Layer):
    moveend = pyqtSignal(dict)
    move = pyqtSignal(dict)
    click = pyqtSignal(dict)

    def __init__(self, latLng: List[float], options=None):
        super().__init__()
        if isinstance(options, type(None)):
            options = {}
        self.latLng = latLng
        self.options = options
        self.opacity = options.get('opacity', 1)
        self.draggable = options.get('draggable', False)
        self._initJs()
        self._connectEventToSignal('move', '_onMove')
        self._connectEventToSignal('moveend', '_onMoveend')
        self._connectEventToSignal('click', '_click')

    @pyqtSlot(QJsonValue)
    def _onMove(self, event):
        self._logger.debug('marker moved. event: {event}'.format(event=event))
        event = self._qJsonValueToDict(event)
        self.latLng = [event["latlng"]["lat"], event["latlng"]["lng"]]
        self.move.emit(event)

    @pyqtSlot(QJsonValue)
    def _onMoveend(self, event):
        self._logger.debug('marker moved. event: {event}'.format(event=event))
        if self.opacity == 0:
            return
        self.moveend.emit({**self._qJsonValueToDict(event), "latLng": self.latLng, "sender": self})

    @pyqtSlot(QJsonValue)
    def _click(self, event):
        self._logger.debug('marker clicked. event: {event}'.format(event=event))
        if self.opacity == 0:
            return
        self.click.emit({**self._qJsonValueToDict(event), "sender": self})

    def _initJs(self):
        leafletJsObject = 'L.marker({latLng}'.format(latLng=self.latLng)
        if self.options:
            leafletJsObject += ', {options}'.format(options=Parser.dict_for_js(self.options))
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

    def setLatLng(self, latLng):
        self.latLng = latLng
        js = '{layerName}.setLatLng({latLng})'.format(
                layerName=self._layerName, latLng=latLng)
        self.runJavaScript(js)
        return self

    def setOpacity(self, opacity):
        self.opacity = opacity
        js = '{layerName}.setOpacity({opacity})'.format(
                layerName=self._layerName, opacity=self.opacity)
        self.runJavaScript(js)
        return self

    def setDragging(self, draggable):
        self.draggable = draggable
        option = 'enable' if self.draggable else 'disable'
        js = '{layerName}.dragging.{option}();'.format(layerName=self._layerName, option=option)
        self.runJavaScript(js)
        return self

    def setIcon(self, icon: Icon):
        js = '{layerName}.setIcon({markerIcon});'.format(layerName=self._layerName, markerIcon=icon._layerName)
        self.runJavaScript(js)
        return self

    def setRotationAngle(self, angle_deg: float):
        js = '{layerName}.setRotationAngle({angle_deg});'.format(layerName=self._layerName, angle_deg=angle_deg)
        self.runJavaScript(js)
        return self

    def setRotationOrigin(self, origin: str):
        js = '{layerName}.setRotationOrigin({origin});'.format(layerName=self._layerName, origin=origin)
        self.runJavaScript(js)
        return self
