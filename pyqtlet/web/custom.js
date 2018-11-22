function copyWithoutCircularReferences(references, object) {
    var cleanObject = {};
    Object.keys(object).forEach(function(key) {
        var value = object[key];
        if (value && typeof value === 'object') {
            if (references.indexOf(value) < 0) {
                references.push(value);
                cleanObject[key] = copyWithoutCircularReferences(references, value);
                references.pop();
            } else {
                cleanObject[key] = '###_Circular_###';
            }
        } else if (typeof value !== 'function') {
            cleanObject[key] = value;
        }
    });
    return cleanObject;
}

// NOTE: There is an assumption here that the map var will be called map
// Might not be the case if there are multiple maps.
function getMapState() {
    var center = map.getCenter();
    var zoom = map.getZoom();
    var bounds = map.getBounds();
    var minZoom = map.getMinZoom();
    var maxZoom = map.getMaxZoom();
    var size = map.getSize();
    var pixelBounds = map.getPixelBounds();
    var pixelOrigin = map.getPixelOrigin();
    var pixelWorldBounds = map.getPixelWorldBounds();
    return {
        center: center,
        zoom: zoom,
        bounds: bounds,
        minZoom: minZoom,
        maxZoom: maxZoom,
        size: size,
        pixelBounds: pixelBounds,
        pixelOrigin: pixelOrigin,
        pixelWorldBounds: pixelWorldBounds
    }
}
