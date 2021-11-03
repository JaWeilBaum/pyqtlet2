import unittest, sys
from pyqtlet2 import L, MapWidget
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)

class MarkerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mapWidget = MapWidget()
        self.map = L.map(self.mapWidget)

    def test_marker_initialization(self):
        test_marker = L.marker((0, 0))



if __name__ == '__main__':
    unittest.main()
