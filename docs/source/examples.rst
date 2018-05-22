Examples
========

Simple Setup App
----------------

This is a simple app that sets up pyqtlet and shows the basic functionality of the
package.

.. code:: python

	import sys
	from PyQt5.QtWidgets import QApplication, QVBoxLayout, QVBoxLayout
	from pyqtlet import L, MapWidget


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

