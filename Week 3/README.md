# ["Raster Function, What's Your Function"](https://www.youtube.com/watch?v=RPoBE-E8VOc)
This lecture will focus on the concept of raster functions

# Preparation
1. Watch:
    - [DevSummit 2018 - Raster Analysis and Image Processing in ArcGIS Enterprise](https://www.esri.com/videos/watch?videoid=zgL7pcQgMbk) 
    - [Raster Analysis with SA and Python](https://www.esri.com/videos/watch?videoid=1jx5uRwLld8)
    - [Raster Function vs. GP](https://www.youtube.com/watch?v=a-lC8_0EyXU)

# Lecture
Raster funciton cans can be applied to imagery layer or embeded into mosaic dataset and image service.
## 1. Applying Raster Functions to elevation
### Applying Raster Functions to the DEM from last week
Using the DEM that we generated for homework from the imagery in Azure storage.
1. Load the DEM into a Map.
2. Open the Raster Functions Pane.
3. Apply Hillshade Raster function.
4. Workflow to embed raster funcitons in mosaic.
5. Add raster function to custom or porject pane.
6. Right click on mosaic dataset.
7. Right click on manage processing templaes
8. Select orage arrow.
9. Add hillshade raster function.

### Image Service
Demonstrate how
1. Searh for the **Terrain** image service in Portal. The URL will be *https://elevation.arcgis.com/arcgis/services/WorldElevation/Terrain/ImageServer*
2. Add to Map
3. Toggle among raster functions that are embeded into the image service.

## 2. Hillshade Algorithm and NAIP NDVI Algorithm in Python using GDAL
1. Walk through accessing NAIP in Azure and creating an NDVI image (gdal_naip_processing.ipynb)
2. Walk through accessing DEM and creating a hillshade (gdal_dem_processing.ipynb)

## 3. Pansharpening SpaceNet Dataset
### Questions
- What is pansharpening?
- Pansharpening methods?
- Pansharpening raster function.
- Pansharpening a SpaceNet image over Georgia.

### Pansharpening Demo
1. Add Khartoum MS image to map
2. Add Khartoum PAN iamge to map
3. Extract bands on MS image using bands 5, 3, and 2.
4. Apply Pansharpening function using Gram-Schmidt and selecting WorldView-3 sensor.
5. Zoom in and compare output and pixel size.
6. Show raster function chain.
7. Save raster function chain so that it can be paramteried and reused.
8. Export raster.

# Exercise\Homework
1. Apply the NDVI raster function to the Landsat OLI Mosaic dataset we created last week. After you apply the NDVI function, apply a colramp to the result to emphasize the contrast. **Submit the Raster Function chain (NDVI + Colorramp).**

2. Using Python GDAL, create a Jupyter Notebook where you write a function that computes the NDVI of a Landsat OLI dataset and takes in the right OLI Bands to compute NDVI for a selected scene. Pull the scenes directly from Landsat in AWS. Do this for the same geographic area where you applied the NDVI function in ArcGIS Pro. How do the results compare? DO they look the same? **Submit the Notebook.**

3. **Challenge** Write a python function to calculate Slope from the digital elevation model.

# Links
