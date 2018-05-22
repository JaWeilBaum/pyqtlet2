# pyqtlet

pyqtlet is a wrapper for Leaflet maps in PyQt5. In construction and design, it mimics the [official leaflet api](http://leafletjs.com/reference-1.3.0.html) as much as possible.

pyqtlet is currently in v0.2.1. To get started, visit the [Getting Started page](http://pyqtlet.readthedocs.io/en/latest/getting-started.html)

Further details about implementation, API docs etc can also be found on the [pyqtlet site](http://pyqtlet.readthedocs.io/en/latest/index.html)

## Installation

``` bash
pip3 install PyQt5
pip3 install pyqtlet
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
        self.marker = L.marker([12.934056, 77.610029])
        self.marker.bindPopup('Maps are a treasure.')
        self.map.addLayer(self.marker)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())
```

## Contributing
In terms of contributing, there is a lot of work that still needs to be done. 
For further details, visit the [contributing page](http://pyqtlet.readthedocs.io/en/latest/contributing.html).
