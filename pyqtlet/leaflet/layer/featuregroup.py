from .layergroup import LayerGroup
from ..layer import marker, vector

class FeatureGroup(LayerGroup):
    """
    Used to group several layers and handle them as one. If you add it to the map, any layers added or removed from the group will be added/removed on the map as well. 
    """

    def _initJs(self):
        leafletJsObject = 'new L.featureGroup()'
        self._createJsObject(leafletJsObject)

    def createAndAddDrawnLayer(self, drawnLayer, options=None):
        layerType = drawnLayer['layerType']
        if layerType == 'polygon':
            coords = drawnLayer['layer']['_latlngs']['0']
            coords = [coords[p] for p in coords]
            self.addLayer(vector.Polygon(coords, options))
        elif layerType == 'marker':
            coords = drawnLayer['layer']['_latlng']
            self.addLayer(marker.Marker(coords, options))
        elif layerType == 'polyline':
            coords = drawnLayer['layer']['_latlngs']
            coords = [coords[p] for p in coords]
            self.addLayer(vector.Polyline(coords, options))
        elif layerType == 'rectangle':
            coords = drawnLayer['layer']['_latlngs']['0']
            coords = [coords[p] for p in coords]
            self.addLayer(vector.Rectangle(coords, options))
        elif layerType == 'circle':
            coords = drawnLayer['layer']['_latlng']
            radius = drawnLayer['layer']['options']['radius']
            self.addLayer(vector.Circle([coords['lat'], coords['lng']], radius))
            
