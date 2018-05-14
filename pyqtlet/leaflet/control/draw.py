from .control import Control
# NOTE: Importing FeatureGroup here may not be the best idea
from ..layer.featuregroup import FeatureGroup

DEFAULT_POSITION = 'topleft'
DEFAULT_CIRCLE = False
DEFAULT_RECTANGLE = False

class Draw(Control):

    def __init__(self, options={}, handleFeatureGroup=True):
        super().__init__()
        self.options = options
        self.handleFeatureGroup = handleFeatureGroup
        self.featureGroup = None
        self._handleOptions()
        self._initJs()
        if handleFeatureGroup:
            self.addedToMap.connect(self.addDrawnToFeatureGroup)

    def _initJs(self):
        jsObject = 'new L.Control.Draw('
        if self.options:
            jsObject += '{options}'.format(options=self._stringifyForJs(self.options))
        jsObject += ')'
        self._createJsObject(jsObject)

    def _handleOptions(self):
        # If there are no options, then we want to set the default options
        self.options['position'] = self.options.get('position', DEFAULT_POSITION)
        draw = self.options.get('draw', {})
        if draw is not False:
            # We want to make sure the user wants draw functionality
            draw['circle'] = draw.get('circle', DEFAULT_CIRCLE)
            draw['rectangle'] = draw.get('rectangle', DEFAULT_RECTANGLE)
            self.options['draw'] = draw
        edit = self.options.get('edit', {})
        if edit is not False:
            # We want to make sure the user wants edit functionality
            featureGroup = edit.get('featureGroup', None)
            if featureGroup is None and self.handleFeatureGroup:
                # If a feature group has not been set, create one and add it
                featureGroup = FeatureGroup()
                edit['featureGroup'] = featureGroup
            self.featureGroup = featureGroup
            self.options['edit'] = edit

    def addDrawnToFeatureGroup(self):
        self.map.addLayer(self.featureGroup)
        self.map.drawCreated.connect(self.featureGroup.createAndAddDrawnLayer)
