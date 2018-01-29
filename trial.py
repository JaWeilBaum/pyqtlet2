import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from pyqtlet import PyQtlet

class TrialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.L = PyQtlet()
        self.setCentralWidget(self.L.widget)
        self.show()
        self.map = self.L.map
        #self.map.addLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png')
        self.map.setView([12.97, 77.59], 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrialWindow()
    sys.exit(app.exec_())
