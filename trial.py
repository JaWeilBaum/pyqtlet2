import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from pyqtlet import MapWidget, L

class TrialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapWidget = MapWidget()
        self.setCentralWidget(self.mapWidget)
        self.map = L.map(self.mapWidget)
        self.map.addOSMBaseMap()
        #self.map.addLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png')
        self.map.setView([12.97, 77.59], 10)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrialWindow()
    sys.exit(app.exec_())
