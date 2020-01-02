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

## Anatomy of the Python Raster Type

### [Raster Type Factory](https://github.com/Esri/raster-types/wiki/RasterTypeFactory-API)

```class RasterTypeFactory:``` - The Raster Type factory is a collection of all the related raster types definitions. The raster type framework extracts information about the raster type from the factory.

```def getRasterTypesInfo(self):``` - This method provides information on the raster type definitions supported within this python module. This method must be defined in order for the class to be recognized as a valid RasterTypeFactory.

You can define the raster type fields that will get added to a mosaic dataset as follows:
```
self.object_auxField = arcpy.Field()
self.object_auxField.name = 'Object'
self.object_auxField.aliasName = 'Object'
self.object_auxField.type = 'String'
self.object_auxField.length = 20
```

Parameters that you will see when you open the ** Add Rasters to Mosaic Dataset** GP tool and select the specified raster funtion.

```'rasterTypeName': 'SINGS',``` - Name of the Raster Type.
```'builderName': 'SINGSBuilder',``` - Name of the class that defines the Python Raster Type.
```'description': ("Supports Spitzer Space Telescop SINGS Data."),``` - Description of Raster Type.
```'dataSourceType': (DataSourceType.File | DataSourceType.Folder),``` - Types of input data sources that you'll see when running **Add Rasters to Mosaic Dataset**.
```'dataSourceFilter': '*.mrf, *.lrc, *.tif',``` - File filters that you can enable.
```'processingTemplates': [``` - Processing templates that you can choose to apply with the Raster Type.
```'fields': [self.object_auxField,``` - The fields to be added to the mosaic dataset table.
