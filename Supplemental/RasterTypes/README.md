# [Raster Types](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/what-is-a-raster-type.htm)
Raster data is added to a mosaic dataset by specifying a raster type. The raster type identifies metadata, such as georeferencing, acquisition date, sensor type, and band wavelengths, along with a raster format. A raster format defines how pixels are stored, such as number of rows and columns, number of bands, actual pixel values, and other raster format-specific parameters. 
You can create custom raster types using Python. For details about how to do this using python, see [raster-types](https://github.com/Esri/raster-types/wiki). This lecture will demonstrate how to do this.

# Lecture 1 - Applying a Custom Python Raster Type
1. Raster Types location in ArcGIS Pro: ```C:\Program Files\ArcGIS\Pro\Resources\Raster\Types```
2. Create a folder in that directors, name it **SINGSTypes**
3. Put the **SpitzerSINGS_RasterType.py** and **SINGS_Default.rft** in that folder.
4. Open ArcGIS Pro. Create a new Project.
5. Create a new mosaic dataset.
6. Add Rasters to the mosaic dataset
![](https://github.com/gbrunner/developing-with-imagery/blob/master/Supplemental/RasterTypes/SINGS_RasterType.png?raw=true)
7. Open the mosaic table and check that the fields are there
![](https://github.com/gbrunner/developing-with-imagery/blob/master/Supplemental/RasterTypes/SINGS_Mosaic.png?raw=true)

