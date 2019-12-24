# Title

# Preparation
1. Watch one of the follwing:
    - [DevSummit 2017 - Writing Image Processing Algorithms using the Python Raster Function](https://www.esri.com/videos/watch?videoid=OgwnKRrVHN0)
    - [UC 2018 - Writing Image Processing Algorithms using the Python Raster Function](https://www.esri.com/videos/watch?videoid=FenT61l-xyQ&title=writing-image-processing-algorithms-using-the-python-raster-function)

# Lecture
For this lecture, we are going to learn how to write image processing algorithms. We will be using Python libraries such as ```numpy``` and ```pickle```, we will build on the concepts we leaned last week, and we will create analysis functions that use Python + ArcGIS. We will start by seeing how to apply a Python Raster Funciton and then we will move onto technicques for developing them using the Landsat OLI mosaics we built in Week 2.

## Imports

We use ```os``` and ```pickle``` to get the data. We will be working with numerical arrays with ```numpy``` and date objects with ```datetime```.

## Apply a Python Raster Function
Create a raster function from a NDVI Python raster function.
NDVI Bands on Landsat OLI are:
- NDVI = (Band 5 – Band 4) / (Band 5 + Band 4)

## Demonstrate writing the Python Raster Function
Jupyter notebooks outline how to use Python and the ```pickle``` module to understand ```pixel_blocks```. I will review four scenarios. 
1. Extracting ```pixel_blocks``` from a single image.
2. Extracting ```pixel_blocks``` from a mosaic dataset.
3. Extracting ```pixel_blocks``` using a raster function that takes in multiple rasters and looks for key metadata.
4. Extracting ```pixel_blocks``` and ```KeyMetadata``` from a mosaic dataset using **Item Grouping**.

These scenarious will demonstrate how you can write custom analysis functions.

## Conclusion
Demonstrate Landsat OLI pixel percentil raster function.

# Homework

1.Create a Python raster function that calculates the hillshade of a single DEM raster or a DEM mosaic. Use the [HydroSHEDS DEM](https://hydrosheds.cr.usgs.gov/dataavail.php) data from last week and the **hillshade** function from the Jupyter notebook. Note that there is another [Hillshade Python Raster Function](https://github.com/Esri/raster-functions/blob/master/functions/Hillshade.py). I don't want you to use this one, i want you to try to write a Python raster function using the code snippet from last week. How does it look? Run the ArcGIS Hillshade function. How do they compare?

2. Create a raster function from the [NVDI python raster function](https://github.com/Esri/raster-functions/blob/master/functions/NDVI.py) and apply it to the Landsat OLI MS QA mosaic that you have created. How does it look?

3. Using the temperature data is the input raster, write a Python Raster Function that converts the raster from showing temperature in celsius to temperature in fahrenheit. The workflow I recommend is to:
    - Use the PRFBasicDebugTemplate.py to extract a pixel block
    - Write a python function that converts the values in that pixel block tofarenheit
    - Move that logic into a Python Raster Function.

4. Building on that raster function, add the option to convert to temperature in [Kelvin](https://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.html)
