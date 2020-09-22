# "That's Meta"

# Class Preparation
- Watch [How Esri Optimizes for Analytics in the Cloud](https://youtu.be/U486YxlDoeM)
- [Slides](https://www.slideshare.net/AmazonWebServices/how-esri-optimizes-massive-image-archives-for-analytics-in-the-cloud-abd402-reinvent-2017)
- [Manageing and Servince Imagery](https://www.esri.com/content/dam/esrisites/en-us/about/events/media/UC-2019/technical-workshops/tw-5755-977.pdf)
- Optionally Wach Anything from [AWS Re-Invent](https://aws.amazon.com/earth/)
- ArcGIS Pro Textbook Chapter on Imagery?

# Lecture 1 - Rasters in the Cloud

## Meta Rasters
  - [NASA MRF](https://github.com/nasa-gibs/mrf)
  - [Meta Raster Format](https://gdal.org/drivers/raster/marfa.html)
## [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
  - We can use GDAL to work directly with raster in cloud storage, such as AWS S3 and Azure Blog storage.
  - Let's clone or download the [OptimizeRasters](https://github.com/Esri/OptimizeRasters) project. We will do this for 2 reasons:
    - We want to use the version of GDAL that comes with it.
    - We will use the tool to upload rasters into S3.
## [GDAL](https://gdal.org/)
GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source License by the Open Source Geospatial Foundation. As a library, it presents a single raster abstract data model and single vector abstract data model to the calling application for all supported formats. It also comes with a variety of useful command line utilities for data translation and processing.
  - [GDAL Virtual File Systems](https://gdal.org/user/virtual_file_systems.html)
  - [gdalinfo.exe](https://gdal.org/programs/gdalinfo.html) 
    - Lists information about a raster dataset.
    - Use GDAL Info to get header info from image in the cloud.
    - ```>"C:\Users\greg6750\Documents\IPython Notebooks\developing-with-imagery\OptimizeRasters\GDAL\bin\gdalinfo.exe" /vsicurl/http://naipblobs.blob.core.windows.net/naip/data/v1/2012/states/mo/mo_1m_2012/36089/m_3608901_se_16_1_20120614.mrf```
  - [gdal_translate.exe](https://gdal.org/programs/gdal_translate.html) 
    - Converts raster data between different formats.
    - Use GDAL Translate to create a raster proxy.
    - Jump into Notebook for example.
    
## MRF
  - Show MRF file structure based on **LE07_L1GT_004025_19990816_20170217_01_T2_B1.mrf** in the **Week 1** folder.
  - Show that ArcGIS Pro recognizes the file.
# COG - [Cloud Optimized GeoTiff](https://www.cogeo.org/)
A Cloud Optimized GeoTIFF (COG) is a regular GeoTIFF file, aimed at being hosted on a HTTP file server, with an internal organization that enables more efficient workflows on the cloud. It does this by leveraging the ability of clients issuing ​HTTP GET range requests to ask for just the parts of a file they need.

## [MRF vs. COG](https://www.element84.com/blog/cloud-optimized-geotiff-vs-the-meta-raster-format)

## [Landsat in AWS](https://aws.amazon.com/blogs/aws/start-using-landsat-on-aws/)
  - [Landsat Path Rows](https://www.usgs.gov/land-resources/nli/landsat/landsat-shapefiles-and-kml-files)
  - Use Python to create proxies form Landsat on AWS
  - Create proxies for multiple TIFs and show that they can be composited into a Landsat type raster.
## [NAIP on Azure](https://azure.microsoft.com/en-us/services/open-datasets/catalog/naip/)
  - [NAIP Index file](https://naipblobs.blob.core.windows.net/naip-index/naip-index.zip)
  
# Lecture 2 - Cloud Storage Connections

## [ArcGIS Cloud Store Connections](https://pro.arcgis.com/en/pro-app/help/projects/connect-to-cloud-stores.htm) for Landsat on AWS and NAIP
  - Using AWS S3 Connection
  - Using Azure Connetion
  - Using Google Cloud Connection?
  
### Connect to **Landsat Archive on AWS**
  - URL: http://landsatarchives.s3.amazonaws.com/
  - Service Endpoint: s3-us-west-2.amazonaws.com
  - Bucketname: landsatarchives
  - Region: US West
  - Datasets:
    - [Landsat 5 (TM)](https://eos.com/landsat-5-tm/)
    - [Landsat 7 (ETM)](https://landsat.gsfc.nasa.gov/the-enhanced-thematic-mapper-plus/)
    
### Connect to **Landsat-8 on AWS
  - Service Endpoint: s3-us-west-2.amazonaws.com
  - Bucketname: landsat-pds
  - Region: US West (Oregon)
  
### NAIP
  - Service Provider: AZURE
  - Bucket Name: naip
  - Access Key ID (Account Name): naipblobs
  - Region: Azure Cloud
  - Service Endpoint: blob.core.windows.net
  
### SpacecNet Public Bucket
  - [SpaceNet on AWS](https://spacenetchallenge.github.io/datasets/datasetHomePage.html)
  - You'll connect to this for your homework\exercise.

# Lecture 3 - Interfacing with the same imagery through GDAL and rasterio in Python

### [GDAL](https://pypi.org/project/GDAL/) and Python
1. Already installed in ArcGIS Pro's Conda environment

### [rasterio](https://rasterio.readthedocs.io/en/stable/) and Python
**Rasterio** is a Python wrapper around *GDAL* that is used specifically for working with raster (imagery) data.

1. Install ```rasterio``` and ```boto3``` into **arcgispro-py3-clone** environment
  - ```conda install boto3```
  - ```conda install -c conda-forge rasterio```. For instructions, go to [```conda install rasterio```](https://github.com/conda-forge/rasterio-feedstock)
2. For more information, please see: **Exercise:** [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)

# Assignment
1. Connect to Landsat-8 on AWS. The connection parameters are:
  - Service Endpoint: s3-us-west-2.amazonaws.com
  - Bucketname: landsat-pds
  - Region: US West (Oregon)
  - Provider Option:
    - ARC_DEEP_CRAWL | NO
    - AWS_NO_SIGN_REQUEST | YES
2. Create an ArcGIS Pro Project where you make a cloud stoage connection to the [spacenet-dataset](https://spacenetchallenge.github.io/datasets/datasetHomePage.html) S3 bucket and you visuzlize a few images from one of the AOIs in the S3 bucket. When connecting to SpaceNet, you don't need to specify the **Region**. Answer the following questions:
- What cities are there? 
- What is the resolution of the image that you selected? 
- What is the Pixel Type of the image that you selected? 
- What is the Bit Depth of the image that you selected?
3. Create a Jupyter Notebook where you list all of the Cloud Optimized GeoTiffs (COG.TIF) Pansaharpened Multispecral (PS-MS) files for **AOI_2_Vegas**. Note, you can do this using arcpy by setting the arcpy workspace to a folder in your *.acs* files as follows:
```
arcpy.env.workspace = "C:\\Users\\greg6750\\Documents\\ArcGIS\\Projects\\AWS Connections\\SpaceNetOnAWS.acs\\AOIs\\AOI_2_Vegas\\PS-RGB"
arcpy.ListRasters()
```
4. For a selected **SpaceNet-Dataset** image, can you write a script or notebook that prints out the information you gathered above? Follow the **gdal_python** or **rasterio_python** tutorials.
5.  (Was working at 2.4 and 2.5, not working at 2.6.x) The cloud storage connection (.acs file) can be used as an arcpy workspace environment variable. Create an ArcGIS Notebook or Jupyter notebook, set the arcpy workspace to be a subfolder within one of your cloud storage connection files, and use arcpy.ListRasters() to generate a list of rasters within the folder.
arcpy.env.workspace = "C:\\Users\\greg6750\\Documents\\ArcGIS\\Projects\\AWS Connections\\SpaceNetOnAWS.acs\\AOIs\\AOI_2_Vegas\\PS-RGB"
arcpy.ListRasters()


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
