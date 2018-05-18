API Documentation
=================

pyqtlet was designed to mimic the `Official Leaflet API <https://leafletjs.com/reference-1.3.0.html>`_
as much as possible, similar to how PyQt5 mimics Qt. This allows a large amount of 
laziness when it actually comes to writing the API docs for the module.

The documentation will only cover what methods have been implemented in pyqtlet.
The details about functionality, options etc. should be obtained from the Leaflet site.
In case of any discrepancies or specially implemented features, they will be mentioned
here in the docs. Otherwise, expect the method to be identical to its JS counterpart.

L.Evented
---------
Baseclass for all pyqtlet objects. All objects will inherit these methods

Methods
^^^^^^^
    * getJsResponse(str:js, function:callback)
        Runs the javascript and then triggers callback with the response
    * runJavaScript(str:js)
        Runs the javascript in the leaflet runtime

L.map
-----
L.map should be initialised with the mapWidget instead of the id of the map div.

Signals
^^^^^^^
    * clicked
    * zoom
    * drawCreated

Methods
^^^^^^^
    * addControl
    * addLayer
    * flyTo
    * getCenter  `[requires callback]`
    * getBounds  `[requires callback]`
    * getZoom  `[requires callback]`
    * getState: `[requires callback]`
        gets center, zoom, bounds, minZoom, maxZoom, size, pixelBounds, pixelOrigin and pixelWorldBounds  
    * hasLayer
    * panTo
    * removeControl
    * removeLayer
    * setMaxBounds
    * setMaxZoom
    * setMinZoom
    * setView

L.Layer
-------
Base class for all layer classes

Methods
^^^^^^^
    * addTo
    * bindPopup
    * bindTooltip
    * removeFrom
    * unbindPopup
    * unbindTooltip

L.tileLayer
-----------

L.marker
--------

Methods
^^^^^^^
    * setLatLng
    * setOpacity

L.circleMarker
--------------

L.polyline
----------

L.polygon
---------

L.rectangle
-----------

L.circle
--------

L.layerGroup
------------

Methods
^^^^^^^
    * addLayer
    * removeLayer
    * toGeoJSON

L.featureGroup
--------------
Inherits from layerGroup

Methods
^^^^^^^
    * createAndAddDrawnLayer(drawnLayer, options=None)
        creates and adds layer to the feature group
        drawnLayer: dict as returned by the 'draw:created' event.

L.control.layers
----------------

L.control.draw
--------------
