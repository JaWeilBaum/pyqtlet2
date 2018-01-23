import os
import time

from PyQt5.QtCore import QObject, QUrl, pyqtSignal
from PyQt5.QtWebEngineWidgets import ( QWebEngineView, QWebEnginePage, QWebEngineSettings, 
                                       QWebEngineScript )

from .web import data
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
        self._page.load(QUrl().fromLocalFile(os.path.join(self._source_dir, 'web', 'map.html')))
        with open(os.path.join(self._source_dir, 'web', 'modules', 'leaflet.js')) as jsSource:
            self.leafletjs = jsSource.read()
        with open(os.path.join(self._source_dir, 'web', 'map.js')) as jsSource:
            self.customjs = jsSource.read()
        self._page.loadStarted.connect(self._pageLoadStart)
        self._page.loadFinished.connect(self._pageLoadComplete)
        self._widget.setPage(self._page)

    def _pageLoadComplete(self):
        print('Actually loaded')
        self._loadFinished = True
        self._page.runJavaScript(self.leafletjs)
        self._page.runJavaScript(self.customjs)

    def _pageLoadStart(self):
        print('Load Started')

