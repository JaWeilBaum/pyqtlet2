"""
Bringing Leaflet maps to PyQt.
"""

__author__ = 'Leon Friedmann <leon.friedmann@tum.de>'
__version__ = '0.7.1'
import sys

if 'PySide6' in sys.modules:
    API = 'PySide6'
elif 'PySide2' in sys.modules:
    API = 'PySide2'
else:
    API = 'PyQt5'

from .mapwidget import MapWidget
from .leaflet import L
