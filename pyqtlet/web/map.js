function getDrawn() {
    var layers = drawnItemsGroup.getLayers()
    var drawnItems = []
    for (var i=0; i<layers.length; i++) {
        drawnItems.push(layers[i].toGeoJSON())
    }
    return JSON.stringify(drawnItems)
}

var map = L.map('map', {
    preferCanvas: true
});
/*
var drawnItemsGroup = new L.FeatureGroup();
map.addLayer(drawnItemsGroup)
var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: drawnItemsGroup
    }
});
map.addControl(drawControl);
map.on(L.Draw.Event.CREATED, function (event) {
    var layer = event.layer;
    drawnItemsGroup.addLayer(layer);
});
*/
