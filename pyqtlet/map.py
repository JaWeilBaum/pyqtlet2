import time

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
        self.zoom = 10

    def setView(self, latLng, zoom='', options=''):
        js = 'map.setView({latLng}'.format(latLng=latLng);
        if zoom:
            js += ', {zoom}'.format(zoom=zoom)
        if options:
            js += ', {options}'.format(options=options)
        js += ');'
        print(js)
        self.webEnginePage.runJavaScript(js)

    def addLayer(self, layer):
        self.webEnginePage.runJavaScript('map.addLayer("{layer}");'.format(layer=layer))

