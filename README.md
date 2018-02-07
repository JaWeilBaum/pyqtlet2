# pyqtlet

pyqtlet is a wrapper for Leaflet maps in PyQt5

## Installation

``` bash
# Not yet implemented
pip3 install pyqtlet
```

## Usage

The library is designed to mimic the leafletjs api to whatever extent it makes sense. For more info, refer to philosohpy.md
``` python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtlet import MapWidget, L


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapWidget = MapWidget()
        self.map = L.map(self.mapWidget)
        self.map.setView([12.97, 77.59], 10)
        osmBaseMap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png')
        self.map.addLayer(osmBaseMap)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow
    sys.exit(app.exec_())
```
For full api spec, visit apidocs.

## v0.1 spec

`pyqtlet` has two classes:
1. `pyqtlet.MapWidget` is a `QWebEngineView`, which is a type of `QWidget`. It will be manipulated like any other `QWidget` and can be added to layouts, stacks etc.
2. `pyqtlet.L` is the python version of all supported leaflet features. It will support objects such as `L.map`, `L.tileLayer` etc. and will replicate the leafletjs api as much as possible.


## Versions
Leaflet version: 1.3.1

Leaflet.draw version: 1.0.2

The further API documentation will be developed along with the code, but will resemble qt and leaflet API in style and design.

This version will __not__ be supporting events.

