# pyqtlet v0.1.0
pyqtlet is a PyQt5 wrapper for [leaflet](leafletjs.com). v0.1 contains the basic functionality of leaflet. There is no support for events in this version.

#### Note
Do not pass pyqtlet objects in options. All bool options for object creation need to be passed as string 'true' or 'false' values.

For all methods that have not yet been implemented in pyqtlet, you can use the `runJavaScript` method on the `L.map` instance. The layer names of the various objects can be accessed fromas the `_layerName` attribute.

```python
custom_js_code = "{marker}.bindPopup('marker')".format(marker=self.marker._layerName)
self.map.runJavaScript(custom_js_code)
```

In case the method has a return value that needs to be calculated from the js pane, the `getJsResponse` method can be used.

```python
custom_js_code = "{marker}.getLatLng()".format(marker=self.marker._layerName)
latLng = self.map.getJsResponse(custom_js_code)
```

## L.map
```python
self.map = L.map(self.mapWidget, options)
```
In the js version, the first argument in the creation is the id of the div. In pyqtlet, this is repaced with the `mapWidget` object from `pyqtlet` which is a `QWebEngineView`, with a `QWebEnginePage`.

[L.map](http://leafletjs.com/reference-1.3.0.html#map-factory)

#### Unsupported Options
- ~~[layers](http://leafletjs.com/reference-1.3.0.html#map-layers)~~
- ~~[renderer](http://leafletjs.com/reference-1.3.0.html#map-layers)~~

### Methods
- [addLayer](http://leafletjs.com/reference-1.3.0.html#map-addlayer)
- [removeLayer](http://leafletjs.com/reference-1.3.0.html#map-removelayer)
- [hasLayer](http://leafletjs.com/reference-1.3.0.html#map-haslayer)
- [setView](http://leafletjs.com/reference-1.3.0.html#map-setview)
- [setZoom](http://leafletjs.com/reference-1.3.0.html#map-setzoom)
- [panTo](http://leafletjs.com/reference-1.3.0.html#map-panto)
- [flyTo](http://leafletjs.com/reference-1.3.0.html#map-flyto)
- [setMaxBounds](http://leafletjs.com/reference-1.3.0.html#map-setmaxbounds) Not working.
- [setMinZoom](http://leafletjs.com/reference-1.3.0.html#map-setminzoom)
- [setMaxZoom](http://leafletjs.com/reference-1.3.0.html#map-setmaxzoom)
- [getCenter](http://leafletjs.com/reference-1.3.0.html#map-getcenter)
- [getBounds](http://leafletjs.com/reference-1.3.0.html#map-getbounds)
- [getZoom](http://leafletjs.com/reference-1.3.0.html#map-getzoom)


## L.layer
Abstract class from which all other layer classes derive.

[L.layer](http://leafletjs.com/reference-1.3.0.html#layer)

### Methods
- [addTo](http://leafletjs.com/reference-1.3.0.html#layer-addto)
- [removeFrom](http://leafletjs.com/reference-1.3.0.html#layer-removefrom)
- [bindPopup](http://leafletjs.com/reference-1.3.0.html#layer-bindpopup) Popup objects not supported
- [unbindPopup](http://leafletjs.com/reference-1.3.0.html#layer-unbindpopup)
- [bindTooltip](http://leafletjs.com/reference-1.3.0.html#layer-bindtooltip) Tooltip objects not supported
- [unbindTooltip](http://leafletjs.com/reference-1.3.0.html#layer-unbindtooltip)

## L.marker
```python
L.marker([12.97, 77.56]).addTo(self.map)
```
[L.marker](http://leafletjs.com/reference-1.3.0.html#marker-l-marker)

#### Unsupported Options
- ~~[icon](http://leafletjs.com/reference-1.3.0.html#marker-icon)~~

### Methods
- [setLatLng](http://leafletjs.com/reference-1.3.0.html#marker-setlatlng)
- [setOpacity](http://leafletjs.com/reference-1.3.0.html#marker-setopacity)

## L.tileLayer
```python
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(self.map);
```
[L.tileLayer](http://leafletjs.com/reference-1.3.0.html#tilelayer)

## L.polyline
```python
# create a red polyline from an array of LatLng points
latlngs = [
    [45.51, -122.68],
    [37.77, -122.43],
    [34.04, -118.2]
    ]
L.polyline(latlngs, {'color': 'red'}).addTo(self.map);
```
[L.polyline](http://leafletjs.com/reference-1.3.0.html#polyline)

## L.polygon
```python
# create a red polygon from an array of LatLng points
latlngs = [
    [45.51, -122.68],
    [37.77, -122.43],
    [34.04, -118.2]
    ]
L.polygon(latlngs, {'color': 'red'}).addTo(self.map);
```
[L.polygon](http://leafletjs.com/reference-1.3.0.html#polygon)

## L.rectangle
```
// define rectangle geographical bounds
bounds = [[54.559322, -5.767822], [56.1210604, -3.021240]]
// create an orange rectangle
L.rectangle(bounds, {color: "#ff7800", weight: 1}).addTo(self.map)
```
[L.rectangle](http://leafletjs.com/reference-1.3.0.html#rectangle)

## L.circle
``` python
L.circle([50.5, 30.5], {radius: 200}).addTo(map);
```
[L.circle](http://leafletjs.com/reference-1.3.0.html#circle)

## L.cirlceMarker
[L.circleMarker](http://leafletjs.com/reference-1.3.0.html#circlemarker)

## L.layerGroup
#### Note:
`L.layerGroup` does not support adding layers in creation right now. It only allows creation of empty layerGroups, to which layers can then be added  and removed.
[L.layerGroup](http://leafletjs.com/reference-1.3.0.html#layergroup)

