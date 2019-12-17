# "That's Meta"

# Class Preparation
- Watch [How Esri Optimizes for Analytics in the Cloud](https://youtu.be/U486YxlDoeM)
- [Slides](https://www.slideshare.net/AmazonWebServices/how-esri-optimizes-massive-image-archives-for-analytics-in-the-cloud-abd402-reinvent-2017)
- [Manageing and Servince Imagery](https://www.esri.com/content/dam/esrisites/en-us/about/events/media/UC-2019/technical-workshops/tw-5755-977.pdf)
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
# COG
  - [Cloud Optimized GeoTiff](https://www.cogeo.org/)
## [Landsat in AWS](https://aws.amazon.com/blogs/aws/start-using-landsat-on-aws/)
  - [Landsat Path Rows](https://www.usgs.gov/land-resources/nli/landsat/landsat-shapefiles-and-kml-files)
  - Use Python to create proxies form Landsat on AWS
  - Create proxies for multiple TIFs and show that they can be composited into a Landsat type raster.
## [NAIP on Azure](https://azure.microsoft.com/en-us/services/open-datasets/catalog/naip/)
  - [NAIP Index file](https://naipblobs.blob.core.windows.net/naip-index/naip-index.zip)

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

## Private Buckets
### Azure Blob Storage
1. Create a storage account, i.e. *jhuimagery*.
2. Create a container, i.e. *naip*.
3. Add rasters to container.
4. Get *Acess Key* from **Access keys**
5. Create **Cloud Storage Connection** file.
![](https://raw.githubusercontent.com/gbrunner/developing-with-imagery/master/Week%202/azure_private_connection.png)

## Optimize Rasters
### OptimizeRasters is a set of tools for converting raster data to optimized Tiled TIF or MRF files, moving data to cloud storage, and creating Raster Proxies. It can do a lot of the work for us!
1. Create an MRF file from NAIP locally. 
2. Add to ArcGIS pro
3. Create an MRF file from NAIP in Azure storage.
4. Add to ArcGIS Pro.

### AWS S3 [Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)

# Assignment
1. Connect to Landsat-8 on AWS. The connection parameters are:
  - Service Endpoint: s3-us-west-2.amazonaws.com
  - Bucketname: landsat-pds
  - Region: US West (Oregon)
  - Provider Option:
    - ARC_DEEP_CRAWL | NO
    - AWS_NO_SIGN_REQUEST | YES
2. Create an ArcGIS Pro Project where you make a cloud stoage connection to the spacenet-dataset S3 bucket and you visuzlize a few images from one of the AOIs in the S3 bucket. Answer the following questions:
- What cities are there? 
- What is the resolution of the image that you selected? 
- What is the Pixel Type of the image that you selected? 
- What is the Bit Depth of the image that you selected?
3. Create a Jupyter Notebook where you list all of the Cloud Optimized GeoTiffs (COG.TIF) Pansaharpened Multispecral (PS-MS) files for **AOI_2_Vegas**. For a selected image, can you write a script that prints out the information you gathered above?
4. Use Optimize Rasters to take a folder of elevation data (*C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Week 4\data\data\dems*), convert to MRF, and load into Azure Storage Account.

~~1. Use GDAL Translate to create raster procxies from a folder of DEMs (*C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Week 4\data\data\dems*). Then, using ArcGIS Pro, create a mosaic dataset from those raster proxies. Build Overviews.~~
~~3. Create a mosaic of all of the NAIP data for a single state. Feel free to use sample notebook and\or NAIP index file.~~

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
