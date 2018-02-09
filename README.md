# pyqtlet

pyqtlet is a wrapper for Leaflet maps in PyQt5. In construction and design, it mimics the [official leaflet api](http://leafletjs.com/reference-1.3.0.html) as much as possible.

pyqtlet is currently in v0.1.0. The functionality that is supported can be found in the [api documentation](https://github.com/skylarkdrones/pyqtlet).

## Installation

``` bash
pip3 install PyQt5
cd /path/to/project
git clone https://github.com/skylarkdrones/pyqtlet.git
```

``` bash
# To test whether it is successfully working
python3 
>>> from pyqtlet import L, MapWidget
>>> # No errors
```

## Usage

``` python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtlet import L, MapWidget


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapWidget = MapWidget()
        self.map = L.map(self.mapWidget)
        self.map.setView([12.97, 77.59], 10)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        L.marker([12.97, 77.59]).addTo(self.map)
        self.setCentralWidget(self.mapWidget)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())
```

## Versions
Leaflet version: 1.3.1

Leaflet.draw version: 1.0.2

