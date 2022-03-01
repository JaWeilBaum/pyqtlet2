import unittest
import sys
from pyqtlet2 import L, MapWidget, API

if API == 'PyQt5:
    from PyQt5.QtWidgets import QApplication
elif API == 'PySide2:
    from PySide2.QtWidgets import QApplication
else:
    from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)


class LayerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mapWidget = MapWidget()
        cls.map = L.map(cls.mapWidget)
        cls.initial_latlng = (0, 0)
        cls.new_latlng = (1, 1)
        cls.initial_layer_latlngs = [(0, 0), (1, 1)]

    def test_marker(self):
        test_marker = L.marker(self.initial_latlng, options={"draggable": False})
        test_marker.setLatLng(self.new_latlng)
        self.assertEqual(test_marker.latLng, self.new_latlng)

        self.assertFalse(test_marker.draggable)
        test_marker.setDragging(True)
        self.assertTrue(test_marker.draggable)

    def test_polyline(self):
        test_polyline = L.polyline(self.initial_layer_latlngs, options=None)
        self.assertEqual(test_polyline.latLngs, self.initial_layer_latlngs)



if __name__ == '__main__':
    unittest.main()
