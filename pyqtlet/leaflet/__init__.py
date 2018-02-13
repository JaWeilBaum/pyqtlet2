from .map import Map
from .layer import LayerGroup
from .layer.tile import TileLayer
from .layer.marker import Marker
from .layer.vector import Circle, CircleMarker, Polygon, Polyline, Rectangle

class L:
    """
    Leaflet namespace that holds reference to all the leaflet objects
    """
    map = Map
    tileLayer = TileLayer
    marker = Marker
    circleMarker = CircleMarker
    polyline = Polyline
    polygon = Polygon
    rectangle = Rectangle
    circle = Circle
    layerGroup = LayerGroup

