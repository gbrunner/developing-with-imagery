# "That's Meta"

# Class Preparation
- Watch [How Esri Optimizes for Analytics in the Cloud](https://youtu.be/U486YxlDoeM)
- [Slides](https://www.slideshare.net/AmazonWebServices/how-esri-optimizes-massive-image-archives-for-analytics-in-the-cloud-abd402-reinvent-2017)
- Optionally Wach Anything from [AWS Re-Invent](https://aws.amazon.com/earth/)
- ArcGIS Pro Textbook Chapter on Imagery?

# Lecture
## Meta Rasters
  - [NASA MRF](https://github.com/nasa-gibs/mrf)
  - [Meta Raster Format](https://gdal.org/drivers/raster/marfa.html)
## [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
  - We can use GDAL to work directly with raster in cloud storage, such as AWS S3 and Azure Blog storage.
## GDAL
  - [GDAL Virtual File Systems](https://gdal.org/user/virtual_file_systems.html)
  - gdalinfo.exe - Use GDAL Info to get header info from image in the cloud
  - gdal_translate.exe - Use GDAL Translate to create a raster proxy.
## MRF
  - Show MRF file structure
## Landsat in AWS
  - [Landsat Path Rows](https://www.usgs.gov/land-resources/nli/landsat/landsat-shapefiles-and-kml-files)
  - Use Python to create proxies form Landsat on AWS
  - Create proxies for multiple TIFs and show that they can be composited into a Landsat type raster.
## NAIP on Azure
  - Use Python to create proxies from NAIP on Azure for Missouri (or perhaps a smaller state).
  - [NAIP Index file](https://naipblobs.blob.core.windows.net/naip-index/naip-index.zip)
  - Mosaic the proxies.
## Finish with creating a [Cloud Store Connection](https://pro.arcgis.com/en/pro-app/help/projects/connect-to-cloud-stores.htm) for Landsat on AWS and NAIP
  - Using AWS S3 Connection
  - Using Azure Connetion
  - Using Google Cloud Connection?
### Connect to **Landsat Archive on AWS**
  - Connection parameters:
  - http://landsatarchives.s3.amazonaws.com/
  - Bucketname: landsatarchives
  - Region: US West
  - Datasets:
    - [Landsat 5 (TM)](https://eos.com/landsat-5-tm/)
    - [Landsat 7 (ETM)](https://landsat.gsfc.nasa.gov/the-enhanced-thematic-mapper-plus/)

# Assignment
1. 
2. Create a mosaic of all of the NAIP data for a single state. Feel free to use sample notebook and\or NAIP index file.

### What Else?
- Processing Functions applied to imagery.
- Download locally?
- Mosaic from local download.
- Segue into next week to mosaic against data in S3
# Datasets
- [Landsat-8 Public Bucket](https://registry.opendata.aws/landsat-8/)
  - https://landsatonaws.com/
- [NAIP is Requester Pays](https://registry.opendata.aws/naip/)
- [USGS Lidar is Requester Pays](https://registry.opendata.aws/usgs-lidar/)
- [Sentinel-2](https://registry.opendata.aws/sentinel-2/)

# Links
- [Earth on AWS - Datasets](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)
