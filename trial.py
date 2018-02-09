import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

from pyqtlet import MapWidget, L

class TrialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapWidget = MapWidget()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.button = QPushButton('clear')
        self.button.clicked.connect(self.buttonPushed)
        self.layout.addWidget(self.mapWidget)
        self.layout.addWidget(self.button)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.map = L.map(self.mapWidget)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.map.setView([12.97, 77.59], 12)
        self.layerGroup = L.layerGroup()
        self.marker = L.circleMarker([12.97, 77.59], {'opacity': 0.7, 'title': 'Blore'})
        self.layerGroup.addLayer(self.marker)
        self.layerGroup.addLayer(L.polyline([[12.97, 77.59],[12.96,77.60]], {'opacity': 1}))
        self.layerGroup.addLayer(L.rectangle([[12.97, 77.59],[12.96,77.60]]))
        self.layerGroup.addLayer(L.polygon([[12.97, 77.59],[12.96,77.60],[12.97, 77.58]]))
        self.layerGroup.addLayer(L.circle([12.97, 77.59], 50))
        self.map.addLayer(self.layerGroup)
        self.show()

    def buttonPushed(self):
        self.map.removeLayer(self.layerGroup)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrialWindow()
    sys.exit(app.exec_())
