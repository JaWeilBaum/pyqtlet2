import json
import logging
import os
import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ... import mapwidget
from ..core import Evented

class Map(Evented):
    """
    L.map equivalent in PyQtlet
    """

    clicked = pyqtSignal(dict)
    zoomend = pyqtSignal(dict)
    drawCreated = pyqtSignal(dict)

    @property
    def layers(self):
        """
        Instead of L.map.eachLayer
        """
        return self._layers

    @property
    def jsName(self):
        return self._jsName

    @pyqtSlot(dict)
    def onClick(self, event):
        self._logger.debug('map clicked. event: {event}'.format(event=event))
        self.clicked.emit(event)

    @pyqtSlot(dict)
    def onDrawCreated(self, event):
        self._logger.debug('draw created. event: {event}'.format(event=event))
        self.drawCreated.emit(event)

    @pyqtSlot(dict)
    def onZoomend(self, event):
        self._logger.debug('map zoomend. event: {event}'.format(event=event))
        self.zoomend.emit(event)

    def __init__(self, mapWidget, options=None):
        super().__init__(mapWidget)
        self._logger = logging.getLogger(__name__)
        self.options = options
        self._layers = []
        self._controls = []
        self._jsName = 'map'
        self._initJs()
        self._connectEventToSignal('click', 'onClick')
        self._connectEventToSignal('zoomend', 'onZoomend')
        self._connectEventToSignal('draw:created', 'onDrawCreated')

    def _initJs(self):
        jsObject = 'L.map("map"'
        if self.options:
            jsObject += ', {options}'.format(options=self._stringifyForJs(self.options))
        jsObject += ')'
        self._createJsObject(jsObject)

    @pyqtSlot(dict)
    def printCoords(self, coords):
        print(coords)

    def setView(self, latLng, zoom=None, options=None):
        js = 'map.setView({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def addLayer(self, layer):
        self._layers.append(layer)
        layer.map = self
        js = 'map.addLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScript(js)

    def removeLayer(self, layer):
        if layer not in self._layers:
            # TODO Should we raise a ValueError here? Or just return
            return
        self._layers.remove(layer)
        layer.map = None
        js = 'map.removeLayer({layerName})'.format(layerName=layer.layerName)
        self.runJavaScript(js)

    def addControl(self, control):
        self._controls.append(control)
        control.map = self
        js = 'map.addControl({controlName})'.format(controlName=control.controlName)
        self.runJavaScript(js)

    def removeControl(self, control):
        if control not in self._controls:
            # TODO Should we raise a ValueError here? Or just return
            return
        self._controls.remove(control)
        control.map = None
        js = 'map.removeControl({controlName})'.format(controlName=control.controlName)
        self.runJavaScript(js)

    def getBounds(self, callback):
        return self.getJsResponse('map.getBounds()', callback)

    def getCenter(self, callback):
        return self.getJsResponse('map.getCenter()', callback)

    def getZoom(self, callback):
        return self.getJsResponse('map.getZoom()', callback)

    def getState(self, callback):
        return self.getJsResponse('getMapState()', callback)

    def hasLayer(self, layer):
        return layer in self._layers

    def setZoom(self, zoom, options=None):
        js = 'map.setZoom({zoom}'.format(zoom=zoom);
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def setMaxBounds(self, bounds):
        js = 'map.setMaxBounds({bounds})'.format(bounds=bounds)
        self.runJavaScript(js)

    def setMaxZoom(self, zoom):
        js = 'map.setMaxZoom({zoom})'.format(zoom=zoom)
        self.runJavaScript(js)

    def setMinZoom(self, zoom):
        js = 'map.setMinZoom({zoom})'.format(zoom=zoom)
        self.runJavaScript(js)

    def panTo(self, latLng, options=None):
        js = 'map.panTo({latLng}'.format(latLng=latLng);
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)

    def setView(self, latLng, zoom=None, options=None):
        js = 'map.flyTo({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        self.runJavaScript(js)




