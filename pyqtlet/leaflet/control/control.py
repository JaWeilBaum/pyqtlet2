import json
import logging
import os
import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ..core import Evented

class Control(Evented):

    # controlId is a static variable shared between all controls
    # It is used to give unique names to controls
    controlId = 0
    # addedToMap and removedFromMap are signals for controls to
    # know when they're added and removed from maps
    addedToMap = pyqtSignal()
    removedFromMap = pyqtSignal()

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, map_):
        self._map = map_
        if map_ is None:
            self.removedFromMap.emit()
        else:
            self.addedToMap.emit()

    @property
    def jsName(self):
        return self._controlName

    @property
    def controlName(self):
        return self._controlName

    @controlName.setter
    def controlName(self, name):
        self._controlName = name

    def __init__(self):
        super().__init__()
        self._controlName = self._getNewControlName()

    def addTo(self, map_):
        map_.addControl(self)

    def removeFrom(self, map_):
        map_.removeControl(self)

    def _getNewControlName(self):
        controlName = 'c{}'.format(self.controlId)
        Control.controlId += 1
        return controlName

