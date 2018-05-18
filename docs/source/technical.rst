Implementation Details
======================
This document is an overview of the technical details of pyqtlet. It covers how the
module is built, the problems that were faced, and how they were tackled.

Structure
---------
The folder and code structure of the leaflet section was designed to mimic that 
of the Leaflet library. I figured they had a better idea on as to why their code 
had been structured that way and didn't want to mess with institutional knowledge 
like that. So now if someone familiar with the leaflet code wants to mess around 
with pyqtlet, they'll know where to find the files they're looking for.

All the leaflet source code is included in the package so that the package is not
dependent on any CDN or network connectivity. 

QWebEngine
----------
Qt offers a `QWebEngine` to handle all the web features. This is obviously the core of
the package. The main widget, :code:`pyqtlet.mapWidget` is subclassed from `QWebEngineView`.

To start off, :code:`mapWidget` loads the html from file, and loads the leaflet canvas 
into itself. To initiate the use of the pyqtlet library, the first pyqtlet object that is
created should be :code:`L.map`. This links all further objects created in the module to
the widget, by assigning the widget as a static variable to :code:`pyqtlet.core.Evented`,
the base class in the module.

Creating the objects in Leaflet
-------------------------------
Since QWebEnginePage allows us to run JavaScript code, it becomes fairly straightforward
to start creating objects from python in the JS runtime. Every object (except abstract ones)
in PyQt, during initialisation, are given their respective jsObject code. So for marker,
the code would be `L.marker`. Evented then has a :code:`_createJsObject` that then runs
the required javascript in the JS runtime.

The names of layers, controls etc are all controlled using static variable in the respective
baseclasses, such that layers are named :code:`l0`, :code:`l1` and so on. The name of the
layer is then stored within the object in the :code:`jsName` attribute.

Python -> JavaScript Communication
-----------------------------------
In order for pyqtlet to offer the functionality of a wrapper around a JS library, it is
necessary to establish communication between JS to send commands and data between the
runtimes. To send commands from Python to JS, we use :code:`QWebEnginePage.runJavaScript`
method. This method can be called with a callback as well. The methods with and without
callback are accessed from :code:`pyqtlet.core.Evented.getJsResponse` and
:code:`pyqtlet.core.runJavaScript` respectively.

All the methods from pyqtlet objects are mostly just calling a `runJavaScript` or 
`getJsResponse` for the appropriate JS code. So map modifying functions like `setView` or
`setMaxZoom` are just calling the same code in JS.

Another thing that we need to keep in mind while communicating with JS is passing objects
as paramenters in options or otherwise. The object needs to be represented in the JS script
string as an object, and not as a string or a python object. `Evented` has a method for
this called `_stringifyForJs`, which recursively goes through dicts and replaces all the
python objects with JS ones and makes it a string.

JavaScript -> Python communication
----------------------------------
Communication from JavaScript is mostly required only for connecting events to their
respective `pyqtSignals`. In order to do this, we need to set up a :code:`QWebChannel`.
What the web channel allows us to do is to trigger python methods from JS code.

In order to do this, we have to first `register` our python objects with the web channel.
This happens in the initialisation of the object, in :code:`Evented._createJsObject`.
It is important to note that only methods of the registered objects can be called from
within JS, so arbitrary code cannot be run, and we cannot pass lambdas, but only methods.

So for every event that leaflet has access to, we have to create a pyqtSignal and a method
that emits the signal. We also then have to connect the event to the method. For that there
is a method :code:`Evented._connectEventToSignal` that does that. It also handles
circular references in the JSON to be returned.

Handling Async
--------------

Solved
^^^^^^
The largest async problem that was faced was nothing to actually do with JavaScript at all.
It was rather to do with Qt. Qt has a few methods that are run asynchronously. One of these
is :code:`QWebEnginePage.load()` which loads html onto the widget. 

The problem with this asynchronicity is that it causes problem with running the next code.
Anstantiating the map ran a `L.map` in the JS runtime before the page (and thus the
leaflet library) was loaded, which caused a widget to just be a blank page.

The solution to this came using :code:`QEventLoop`. An infinite loop was created that only
quit when the web page emitted a :code:`loadFinished` signal. This ensured that the interpreter
waited until the html was loaded and only them progressed.

Unsolved
^^^^^^^^
The problem that still has not been solved is how to handle the async running of `runJavaScript`.
If we want the method to return a value from JS, then a similar approach doesn't seem to work.
I have tried numerous combinations of threads, signals, callbacks and channel objects, but 
none of them seem to be able to emit the signal which would break the infinite loop that is
waiting for a response before it can terminate.

The problem that I'm looking to solve is how a method can run some JS code, and then return
the response from that same code.

********

Overall building this package was a great exercise that I learnt a lot out of. I hope
it helps you in creating some great apps. In case you have any feedback on how this whole
thing can be implemented better, please raise an issue and let me know, or a pull request 
if you are in the mood for something like that.
