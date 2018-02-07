import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

from pyqtlet import MapWidget, L

class TrialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapWidget = MapWidget()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.button = QPushButton('push')
        self.button.clicked.connect(self.buttonPushed)
        self.layout.addWidget(self.mapWidget)
        self.layout.addWidget(self.button)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.map = L.map(self.mapWidget)
        self.baseLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png')
        self.map.addLayer(self.baseLayer)
        self.map.setView([12.97, 77.59], 10)
        self.marker = L.marker([12.97, 77.59], {'opacity': 0.7, 'title': 'Blore'})
        self.map.addLayer(self.marker)
        self.show()

    def buttonPushed(self):
        self.map.removeLayer(self.marker)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrialWindow()
    sys.exit(app.exec_())
