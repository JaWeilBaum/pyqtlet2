from PyQt5.QtCore import QObject


class Map(QObject):
    """
    L.map equivalent in PyQtlet
    """
    def __init__(self, parent, webEnginePage, webChannel):
        self.parent = parent
        self.webEnginePage = webEnginePage
        self.webChannel = webChannel
        self.pageLoaded = False

    def setView(self, coords):
        if self._checkPageLoaded():
            self.webEnginePage.runJavaScript('map.setView({coords});'.format(coords=coords))

    def addLayer(self, layer):
        if self._checkPageLoaded():
           self.webEnginePage.runJavaScript('map.addLayer("{layer}");'.format(layer=layer))

    def _checkPageLoaded(self):
        if not self.pageLoaded:
            while not self.parent.loadFinished:
                print('page not yet loaded')
                pass
            self.pageLoaded = True
            print('page loaded')
        return self.pageLoaded
