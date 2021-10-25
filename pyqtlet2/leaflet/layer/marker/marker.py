from ..layer import Layer

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QJsonValue

class Marker(Layer):
    moveend = pyqtSignal(dict)
    move = pyqtSignal(dict)
    click = pyqtSignal(dict)

    def __init__(self, latLng, options=None):
        super().__init__()
        self.latLng = latLng
        self.options = options
        self.opacity = options.get('opacity', 0)
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
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

    def setLatLng(self, latLng):
        js = '{layerName}.setLatLng({latLng})'.format(
                layerName=self._layerName, latLng=latLng)
        self.runJavaScript(js)

    def setOpacity(self, opacity):
        self.opacity = opacity
        js = '{layerName}.setOpacity({opacity})'.format(
                layerName=self._layerName, opacity=self.opacity)
        self.runJavaScript(js)
