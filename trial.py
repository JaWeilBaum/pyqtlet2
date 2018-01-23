import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from pyqtlet import PyQtlet

class TrialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pyqtlet = PyQtlet()
        self.setCentralWidget(self.pyqtlet.widget)
        self.show()
        self.map = self.pyqtlet.map
        self.map.addLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png')
        #self.map.setView([51.505, -0.09])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrialWindow()
    sys.exit(app.exec_())
