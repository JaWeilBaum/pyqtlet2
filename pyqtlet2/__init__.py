"""
Bringing Leaflet maps to PyQt.
"""

__author__ = 'Leon Friedmann <leon.friedmann@tum.de>'
__version__ = '0.7.0'
import sys

if 'PySide6' in sys.modules:
    API = 'PySide6'
else:
    API = 'PyQt5'

from .mapwidget import MapWidget
from .leaflet import L
