import json
import logging
import os
import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ..core import Evented

class Control(Evented):

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, map_):
        self._map = map_

    def __init__(self, options=None):
        super().__init__()
        self.options = options

    def addTo(self, map_):
        map_.addControl(self)

    def removeFrom(self, map_):
        map_.removeControl(self)

