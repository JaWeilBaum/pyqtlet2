var map = L.map('map');
var drawnItemsLayer = new L.FeatureGroup();
map.addLayer(drawnItemsLayer)
var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: drawnItemsLayer
    }
});
map.addControl(drawControl);
map.on(L.Draw.Event.CREATED, function (event) {
    var layer = event.layer;
    drawnItemsLayer.addLayer(layer);
});
