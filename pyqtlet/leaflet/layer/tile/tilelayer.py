from . import GridLayer

class TileLayer(GridLayer):
    def __init__(self, urlTemplate, options=''):
        self.urlTemplate = urlTemplate
        self.options = options

