# Using Imagery with the [ArcGIS API for JavaScript](https://developers.arcgis.com/javascript/) and [ArcGIS REST API](https://developers.arcgis.com/rest/)

:bookmark: <https://developers.arcgis.com/javascript/>

:bookmark: <https://developers.arcgis.com/rest/>

## Hello, web mapping

(_oh, and_ `HTML` _and_ `CSS` _and_ `JavaScript`)

A great place to start making your own interactive (and free!) web maps is the ArcGIS API for JavaScript (JSAPI).

1. Check out the quick start tutorial: <https://developers.arcgis.com/javascript/latest/guide/quick-start/#3.-hello-world>

2. Walk through other tutorials that pique your interest: <https://developers.arcgis.com/javascript/latest/guide/>

And for a quick primer on related web development topics, head over to this lecture: <https://github.com/gbrunner/intro-prog-for-gis-rs/tree/master/Week%2013>

## Server, please give me pixels

The data we rely on in a web map often comes from :cloud: servers :cloud: that give us _services_ to interact with. The ArcGIS REST API is a documented system of standards for how ArcGIS servers and services are organized and what they can do for you through HTTP network requests.

Right now we are focused on the **Image Service** within the ArcGIS REST API. <https://developers.arcgis.com/rest/services-reference/image-service.htm>

ArcMap, Pro, the ArcGIS API for Python, and other parts of the Esri software ecosystem can all talk to an Image Service. Each of these make your life easier by not making you worry about all the under-the-hood HTTP network requests that are needed to transfer remote sensing pixel information between a server and your software.

The JSAPI is no different: it enables you to put pixels on a web map with its own `ImageryLayer` module that communicates with an Image Service.

1. [This "Intro to ImageryLayer" sample](https://developers.arcgis.com/javascript/latest/sample-code/layers-imagerylayer/index.html) shows how to quickly add an NLCD land cover layer to a map. Click on "Explore in the sandbox" and find the URL to the Image Service of this land cover layer. **HINT:** it will always end in `.../ImageServer`.

2. Open the documentation page and the layer URL side-by-side to help make sense of everything an Image Service can do.
    - <https://developers.arcgis.com/rest/services-reference/image-service.htm>
    - <https://sampleserver6.arcgisonline.com/arcgis/rest/services/NLCDLandCover2001/ImageServer>

3. Look at [this "Export Image" operation](https://sampleserver6.arcgisonline.com/arcgis/rest/services/NLCDLandCover2001/ImageServer/exportImage?bbox=-2364615.0,256035.0,2266845.0,3180435.0). The "Export Image" operation is the most common way to transfer pixels from the server to your web map, and the JSAPI uses this whenever the web map is panned and zoomed to request and then display the latest pixels at that map extent.

4. Explore a few more [`ImageryLayer` JSAPI samples](https://developers.arcgis.com/javascript/latest/sample-code/?search=ImageryLayer).

## Do more with pixels

_TODO: JSAPI ImageryLayer with a popup to show how pixel data is queried at a point location_

_TODO: JSAPI ImageryLayer with a server side raster function (`renderingRule`) to ask the server to change pixels before they get to you_

_TODO: JSAPI ImageryLayer with a `pixelFilter` function to show how to access/manipulate arrays of pixel data with JS code in the browser_
