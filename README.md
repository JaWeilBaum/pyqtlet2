# pyqtlet2

pyqtlet is a wrapper for Leaflet maps in PyQt5. In construction and design, it mimics the [official leaflet api](http://leafletjs.com/reference-1.3.0.html) as much as possible.

## About

This is a fork of the repository pyqtlet from @skylarkdrones. Since the original repository is not further maintained. Since I find this package very usefull for a map implementation in the QT environment, I want to further develop this package. If you want to extend this package feel free to get in contact with me or create a Issue/Pull Request with a change! 

## Installation

``` bash
pip3 install PyQt5
pip3 install PyQtWebEngine
pip3 install pyqtlet2
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
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet2 import L, MapWidget


class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        # Working with the maps with pyqtlet
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

## Addtional Leaflet Packages
- Leaflet.draw (Version 0.4.14) - https://github.com/Leaflet/Leaflet.draw
- Leaflet.RotatedMarker (Version 0.2.0) - https://github.com/bbecquet/Leaflet.RotatedMarker

## Using Unimplemented Leaflet Features
At this time, there is noone actively adding features to pyqtlet. This means that there
are a lot of Leaflet features that are not implemented in pyqtlet. However, there is still
a way to access these features via the `runJavaScript` api. This allows arbitrary code to
be run within the map window.

For example, if we want to change the marker icon in the above example, add the following
2 lines of code after the `self.map.addLayer(self.marker)` statement.

``` python
        # Create a icon called markerIcon in the js runtime.
        self.map.runJavaScript('var markerIcon = L.icon({iconUrl: "https://leafletjs.com/examples/custom-icons/leaf-red.png"});')
        # Edit the existing python object by accessing it's jsName property
        self.map.runJavaScript(f'{self.marker.jsName}.setIcon(markerIcon);')
```

This technique will allow users to use all the features available in leaflet.

## Contributors

A big thank you, goes to all the contributors of this project!

<a href="https://github.com/JaWeilBaum/pyqtlet2/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JaWeilBaum/pyqtlet2" />
</a>

## Contributing
In terms of contributing, there is a lot of work that still needs to be done. 
Specifically, there are a lot of leaflet features that need to be ported into pyqtlet. All contributions welcome.
