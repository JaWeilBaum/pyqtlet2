import os
import time

from PyQt5.QtCore import QEventLoop, QObject, QUrl, pyqtSignal
from PyQt5.QtWebEngineWidgets import ( QWebEngineView, QWebEnginePage, QWebEngineSettings, 
                                       QWebEngineScript )

from .map import Map


class PyQtlet(QObject):
    """
    The PyQtlet class houses the leaflet map widget that can be added
    to any Qt layout, as well as all the functions that manipulate the
    map, by adding/removing shapes and all other defined functions.
    It is a wrapper around leaflet.js and a few leaflet plugins. Over 
    time, more plugins can be added.
    """

    @property
    def widget(self):
        return self._widget

    @property
    def map(self):
        return self._map

    @property
    def loadFinished(self):
        return self._loadFinished

    def __init__(self):
        super().__init__()
        self._loadFinished = False
        self._source_dir = os.path.dirname(__file__)
        self._widget = QWebEngineView()
        self._page = QWebEnginePage()
        self._initialiseQtElements()
        self._map = Map(self, self._page, 'webchannel')

    def _initialiseQtElements(self):
        init_loop = QEventLoop()
        self._page.load(QUrl().fromLocalFile(os.path.join(self._source_dir, 'web', 'map.html')))
        self._page.loadFinished.connect(init_loop.quit)
        init_loop.exec()
        self._widget.setPage(self._page)
        self._loadJavascript()

    def _loadJavascript(self):
        with open(os.path.join(self._source_dir, 'web', 'modules', 'leaflet', 'leaflet.js')) as jsSource:
            leafletjs = jsSource.read()
        self._page.runJavaScript(leafletjs)
        with open(os.path.join(self._source_dir, 'web', 'map.js')) as jsSource:
            customjs = jsSource.read()
        self._page.runJavaScript(customjs)
        self._page.runJavaScript("""L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {maxZoom:20, subdomains:['mt0', 'mt1', 'mt2', 'mt3']}).addTo(map);""")

