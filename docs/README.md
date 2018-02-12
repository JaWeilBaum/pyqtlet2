# pyqtlet v0.1.0
pyqtlet is a PyQt5 wrapper for [leaflet](leafletjs.com). v0.1 contains the basic functionality of leaflet. There is no support for events in this version.

#### Note
All bool options for object creation need to be passed as string 'true' or 'false' values.

## L.map
```python
self.map = L.map(self.mapWidget, options)
```
In the js version, the first argument in the creation is the id of the div. In pyqtlet, this is repaced with the `mapWidget` object from `pyqtlet` which is a `QWebEngineView`, with a `QWebEnginePage`.

[L.map](http://leafletjs.com/reference-1.3.0.html#map-factory)

#### Unsupported Options
~~[layers](http://leafletjs.com/reference-1.3.0.html#map-layers)~~
~~[renderer](http://leafletjs.com/reference-1.3.0.html#map-layers)~~

### Methods
- [addLayer](http://leafletjs.com/reference-1.3.0.html#map-addlayer)
- [removeLayer](http://leafletjs.com/reference-1.3.0.html#map-removelayer)
- [hasLayer](http://leafletjs.com/reference-1.3.0.html#map-haslayer)
- [setView](http://leafletjs.com/reference-1.3.0.html#map-setview)
- [setZoom](http://leafletjs.com/reference-1.3.0.html#map-setzoom)
- [panTo](http://leafletjs.com/reference-1.3.0.html#map-panto)
- [flyTo](http://leafletjs.com/reference-1.3.0.html#map-flyto)
- [setMaxBounds](http://leafletjs.com/reference-1.3.0.html#map-setmaxbounds)
- [setMinZoom](http://leafletjs.com/reference-1.3.0.html#map-setminzoom)
- [setMaxZoom](http://leafletjs.com/reference-1.3.0.html#map-setmaxzoom)
- [getCenter](http://leafletjs.com/reference-1.3.0.html#map-getcenter)
- [getZoom](http://leafletjs.com/reference-1.3.0.html#map-getzoom)
- [getBounds](http://leafletjs.com/reference-1.3.0.html#map-getBounds)
