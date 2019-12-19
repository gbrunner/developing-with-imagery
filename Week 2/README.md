# How did they do that?
How did Microsoft get those NAIP MRFs into blob storage? The theme of this lecture is working towards understanding how to create image services that use imagery in S3 by first understanding how the imagery gets into S3.

# Preparation
1. Read:
    - [Managing Imagery in the Cloud](http://proceedings.esri.com/library/userconf/proc17/tech-workshops/tw_630-625.pdf)
    - [MRF](https://community.esri.com/thread/212729-mrf-s3-mosaics-caches-and-optimization)
    - [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
    - [MDCS](https://github.com/Esri/mdcs-py)
2. Watch:
    - [Optimize Rasters](https://www.youtube.com/watch?v=NEu0BYA1jAA)

# Lecture - Interfacing with imagery in Azure, AWS, and Google Cloud

## Part 1 - Private Storage
*For this class, all students will need azure storage accounts.*

## Private Buckets

### Azure Blob Storage
In this demo, I will create a blob storage container in my Azure storage accound, *jhuimagery*.

1. Create a storage account, i.e. *jhuimagery*.
    - Resource Group: greg's courses
    - status: Available
    - Location: Central US, East US 2
    - Performance/Access tier: Standard/Hot
    - Replication: Read-access geo-redundant storage (RA-GRS)
    - Account kind: BlobStorage

2. Create a container
    - Select the **+ Container** button.
    - Give the **Container** a name.
    - Select a private **Container**.

## Part 2 - Geting Data into the Azure Storage using [OptimizeRasters](https://github.com/Esri/OptimizeRasters)
OptimizeRasters is a set of tools for converting raster data to optimized Tiled TIF or MRF files, moving data to cloud storage, and creating Raster Proxies. It can do a lot of the work for us!

In this demo, I will upload some astronomy images into a blob storage container and then visualize them in ArcGIS Pro and Jupyter.

1. Create a profile using the **Profile Editor** tool in **Optimize Rasters**
    - Profile Type: Microsoft Azure
    - Profile Name: *User Defined*
    - Access/Account Key ID: *name of container*
    - Secret Access Account Key: *Key 1*

2. Use Optimize Rasters to Convert to MRF
    ![](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%202/sings_to_local.png?raw=true)
3. Use Optimize Rasters to convert to MRF add rasters to the **Container**
    ![](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%202/sings_to_azure.png?raw=true)
    
4. View results in ArcGIS Pro
    - Create a **Cloud Storage Connection** file to your private container.
    - Service Provider: Azure
    - Container Name: *User Defined*
    - Access/Account Key ID: *name of container*
    - Secret Access Account Key: *Key 1*
    
![](https://raw.githubusercontent.com/gbrunner/developing-with-imagery/master/Week%202/azure_private_connection.png)

## Part 3 - ArcGIS Mosaic Datasets
1. Build a mosaic from the NAIP on Azure raster proxies.
2. Build a mosaic and add a single AWS band collection manually.
3. Build a second mosaic and add an entire path row over **your_aoi_here**
4. Introduc [MDCS](https://github.com/Esri/mdcs-py)
5. Show configuration of MDCS and resulting mosaic.

# Exercises and Homework
1. Create a private container in your Azure Blob Storage account named **dem**
2. Using Optimize Rasters, convert the elevation models in *C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Week 4\data\data\dems* to COG or MRF and upload them into **dem**
3. Using ArcGIS Pro, create a mosaic dataset from the rasters in **dem**. Be sure to build pyramids and overviews. Where did you store your overviews?
4. Create a Landsat Mosaic from OLI data...


# Github Links
  - [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
  - [MDCS](https://github.com/Esri/mdcs-py)
