import json
import logging
import os
import time

from qtpy.QtCore import Slot, Signal, QJsonValue

from ... import mapwidget
from ..core import Evented
from ..layer import Layer


class Map(Evented):
    '''
    .. module:: pyqtlet2

    pyqtlet2 equivalent of L.map

    Map element has to be the first pyqtlet2 object to be initiated.

    .. note::
        Further documentation can be found at the official leaflet API.

    :param pyqtlet2.MapWidget mapWidget: The mapwidget object
        Should only be sent once, when the first object is being 
        initialised.

    :param dict options: Options for initiation (optional)
    '''

    clicked = Signal(dict)
    zoom = Signal(dict)
    drawCreated = Signal(dict)
    right_mouse_clicked = Signal(dict)
    mapWidgetCounter = 0

    @property
    def layers(self):
        """
        Instead of L.map.eachLayer
        """
        return self._layers

    @property
    def jsName(self):
        '''
        Name of the Leaflet element
        '''
        return self._jsName

    @Slot(QJsonValue)
    def _onClick(self, event):
        self._logger.debug('map clicked. event: {event}'.format(event=event))
        self.clicked.emit(self._qJsonValueToDict(event))
        
    @Slot(QJsonValue)
    def _onRightClick(self, event):
        self._logger.debug('map clicked. event: {event}'.format(event=event))
        self.right_mouse_clicked.emit(self._qJsonValueToDict(event))

    @Slot(QJsonValue)
    def _onDrawCreated(self, event):
        self._logger.debug('draw created. event: {event}'.format(event=event))
        self.drawCreated.emit(self._qJsonValueToDict(event))

    @Slot(QJsonValue)
    def _onZoom(self, event):
        self._logger.debug('map zoom. event: {event}'.format(event=event))
        self.zoom.emit(self._qJsonValueToDict(event))

    def __init__(self, mapWidget, options=None):
        '''
        pyqtlet2 equivalent of L.map

        Map element has to be the first pyqtlet2 object to be initiated.

        :param pyqtlet2.MapWidget mapWidget: The mapwidget object
            Should only be sent once, when the first object is being
            initialised.

        :param dict options: Options for initiation (optional)

        .. note
            Further documentation can be found at the official leaflet API.
        '''

        super().__init__(mapWidget, Map.mapWidgetCounter)
        self.mapWidgetIndex = Map.mapWidgetCounter
        Map.mapWidgetCounter += 1
        self._logger = logging.getLogger(__name__)
        self.options = options
        self._layers = []
        self._controls = []
        self._jsName = 'map'
        self._initJs()
        self._connectEventToSignal('click', '_onClick', self.mapWidgetIndex)
        self._connectEventToSignal('contextmenu', '_onRightClick', self.mapWidgetIndex)
        self._connectEventToSignal('zoom', '_onZoom', self.mapWidgetIndex)
        self._connectEventToSignal('draw:created', '_onDrawCreated', self.mapWidgetIndex)

    def _initJs(self):
        jsObject = 'L.map("map"'
        if self.options:
            jsObject += ', {options}'.format(options=self._stringifyForJs(self.options))
        jsObject += ')'
        self._createJsObject(jsObject, self.mapWidgetIndex)

    def setView(self, latLng, zoom=None, options=None):
        js = 'map.setView({latLng}'.format(latLng=latLng)
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js, self.mapWidgetIndex)
        return self

    def runJavaScriptForMap(self, js):
        self.runJavaScript(js, self.mapWidgetIndex)

    def addLayer(self, layer: Layer):
        self._layers.append(layer)
        layer.map = self
        layer._initJs()
        js = 'map.addLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScriptForMap(js)
        layer._initPopupAndTooltip()
        return self

    def removeLayer(self, layer):
        if layer not in self._layers:
            # TODO Should we raise a ValueError here? Or just return
            return
        self._layers.remove(layer)
        layer.map = None
        js = 'map.removeLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScriptForMap(js)
        return self

    def addControl(self, control):
        self._controls.append(control)
        control.map = self
        control._initJs()
        js = 'map.addControl({controlName})'.format(controlName=control.controlName)
        self.runJavaScriptForMap(js)
        return self

    def removeControl(self, control):
        if control not in self._controls:
            # TODO Should we raise a ValueError here? Or just return
            return
        self._controls.remove(control)
        control.map = None
        js = 'map.removeControl({controlName})'.format(controlName=control.controlName)
        self.runJavaScriptForMap(js)
        return self

    def getJsresponseForMap(self, js, callback):
        return self.getJsResponse(js, self.mapWidgetIndex, callback)

    def getBounds(self, callback):
        return self.getJsresponseForMap('map.getBounds()', callback)

    def getCenter(self, callback):
        return self.getJsresponseForMap('map.getCenter()', callback)

    def getZoom(self, callback):
        return self.getJsresponseForMap('map.getZoom()', callback)

    def getState(self, callback):
        return self.getJsresponseForMap('getMapState()', callback)

    def hasLayer(self, layer):
        return layer in self._layers

    def setZoom(self, zoom, options=None):
        js = 'map.setZoom({zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScriptForMap(js)
        return self

    def setMaxBounds(self, bounds):
        js = 'map.setMaxBounds({bounds})'.format(bounds=bounds)
        self.runJavaScriptForMap(js)
        return self

    def fitBounds(self, bounds):
        js = 'map.fitBounds({bounds})'.format(bounds=bounds)
        self.runJavaScriptForMap(js)
        return self

    def setMaxZoom(self, zoom):
        js = 'map.setMaxZoom({zoom})'.format(zoom=zoom)
        self.runJavaScriptForMap(js)
        return self

    def setMinZoom(self, zoom):
        js = 'map.setMinZoom({zoom})'.format(zoom=zoom)
        self.runJavaScriptForMap(js)
        return self

    def panTo(self, latLng, options=None):
        js = 'map.panTo({latLng}'.format(latLng=latLng)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScriptForMap(js)
        return self

    def flyTo(self, latLng, zoom=None, options=None):
        js = 'map.flyTo({latLng}'.format(latLng=latLng)
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScriptForMap(js)
        return self
