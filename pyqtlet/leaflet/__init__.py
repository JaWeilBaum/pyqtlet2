from .map import Map
from .layer import LayerGroup, FeatureGroup, imageOverlay
from .layer.tile import TileLayer
from .layer.marker import Marker
from .layer.vector import Circle, CircleMarker, Polygon, Polyline, Rectangle
from .control import Control

class L:
    """
    Leaflet namespace that holds reference to all the leaflet objects
    """
    map = Map
    tileLayer = TileLayer
    imageOverlay = imageOverlay
    marker = Marker
    circleMarker = CircleMarker
    polyline = Polyline
    polygon = Polygon
    rectangle = Rectangle
    circle = Circle
    layerGroup = LayerGroup
    featureGroup = FeatureGroup
    control = Control

