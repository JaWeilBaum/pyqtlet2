from .map import Map
from .layer.tile import TileLayer
from .layer.marker import Marker
from .layer.vector import CircleMarker, Polygon, Polyline, Rectangle
from .control import Control
from .draw import Draw

class L:
    map = Map
    tileLayer = TileLayer
    marker = Marker
    circleMarker = CircleMarker
    polyline = Polyline
    polgyon = Polygon
    rectangle = Rectangle
