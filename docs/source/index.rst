Pyqtlet
=======

pyqtlet brings `Leaflet <https://leafletjs.com/>`_ maps to `PyQt5 <http://pyqt.sourceforge.net/Docs/PyQt5/introduction.html>`_.

`Leaflet <https://leafletjs.com/>`_ is the most popular mapping library on the web. It has most mapping features that you might need, excellent documentation, and a host of plugins. In contstruction and design, pyqtlet attempts to mimic the `official Leaflet API <http://leafletjs.com/reference-1.3.0.html>`_ as much as possible.

pyqtlet allows you to bring in these leaflet maps into PyQt5 in just a couple of lines. It provides a mapWidget (which is a QWidget) as well as a namespace (L) in order to mimic the Leaflet API.

.. code-block:: python

    from pyqtlet import L, MapWidget

    class Application(QMainWindow):
        ...
        self.mapWidget = MapWidget()
        self.map = L.map(self.mapWidget)
        self.map.setView([12.97, 77.59], 10)
        ...
        self.layout.add(self.mapWidget)


If you have are just starting out, you might want to start off with the :doc:`getting-started` page.

.. toctree::
    :hidden:
    
    getting-started
    api-docs
    examples
    tutorials
    technical
    contributing
