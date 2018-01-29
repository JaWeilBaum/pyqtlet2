# pyqtlet

pyqtlet is a wrapper for Leaflet maps in PyQt5

## v0.1 spec

PyQtlet is a `QObject`. It has two primary attributes.
1. PyQtlet.widget is a `QWebEngineView`, which is a type of `QWidget`. It will be manipulated like any other `QWidget` and can be added to layouts, stacks etc.
2. PyQtlet.map is a custom object created for this module and will behave similar to a `L.map` object as created by Leaflet.

At a higher level, the functionality offered by v0.1 will be as follows:

- Layers: get, add, remove
- Markers: get, add, remove
- CircleMarkers: get, add, remove
- Lines: get, add, remove
- Polygon: get, add, remove

This version will __not__ be supporting styling or events.

The further API documentation will be developed along with the code, but will resemble qt and leaflet API in style and design.
