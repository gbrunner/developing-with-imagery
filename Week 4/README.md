# Title

# Preparation
1. Watch:
    - [Writing Image Processing Algorithms using the Python Raster Function](https://www.esri.com/videos/watch?videoid=OgwnKRrVHN0)
    - [UC 2018 - Writing Image Processing Algorithms using the Python Raster Function](https://www.esri.com/videos/watch?videoid=FenT61l-xyQ&title=writing-image-processing-algorithms-using-the-python-raster-function)

# Lecture
## Apply a Python Raster Function
Take an existing PRF, create the raster function template, and apply it to a raster. Then explain the pieces of the raster function.
1. Using a [HydroSHEDS DEM](https://hydrosheds.cr.usgs.gov/dataavail.php)
2. Create a hillshade raster function from the [Hillshade Python Raster Function](https://github.com/Esri/raster-functions/blob/master/functions/Hillshade.py)
3.

## Demonstrate writing the Python Raster Function
1. Extract pixel blocks
2. Look at pixel blocks in a notebook.
3. Write algorithm
4. Put algorithm into PRF.

## Extract pixel blocks from other datasets
1. Landsat
2. Thematic (precipitation)
3. Temperature

# Homework
1. Using the temperature data is the input raster, write a Python Raster Function that converts the raster from showing temperature in celsius to temperature in fahrenheit. The workflow I recommend is to:
- Use the PRFBasicDebugTemplate.py to extract a pixel block
- Write a python function that converts the values in that pixel block tofarenheit
- Move that logic into a Python Raster Function.

2. Building on that raster function, add the option to convert to temperature in [Kelvin](https://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.html)

# Challenge

# 3 Sample Raster Functions
## Processing an Elevation Model

## Processing a Landsat Scene

## Processing Temporal Data (Landsat)
