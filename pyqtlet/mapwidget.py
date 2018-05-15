import os
import time

from PyQt5.QtCore import QEventLoop, QObject, QUrl, pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import ( QWebEngineView, QWebEnginePage, QWebEngineSettings, 
                                       QWebEngineScript )


class MapWidget(QWebEngineView):
    """
    The MapWidget class is a QWebEngineView that houses the leaflet map.
    Since it is a QWidget, it can be added to any QLayout.
    """

    @property
    def page(self):
        return self._page

    @property
    def channel(self):
        return self._channel

    def __init__(self):
        super().__init__()
        self._page = QWebEnginePage()
        self.setPage(self._page)
        self._channel = QWebChannel()
        self._page.setWebChannel(self._channel)
        self._loadPage()

    def _loadPage(self):
        html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web', 'map.html')
        # QEventLoop is used to make the page loading behave syncronously
        init_loop = QEventLoop()
        self._page.loadFinished.connect(init_loop.quit)
        self._page.load(QUrl().fromLocalFile(html_path))
        init_loop.exec()

