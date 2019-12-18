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

## Part 1 - Geting Data into the Cloud

## Optimize Rasters
### OptimizeRasters is a set of tools for converting raster data to optimized Tiled TIF or MRF files, moving data to cloud storage, and creating Raster Proxies. It can do a lot of the work for us!
1. Create an MRF file from NAIP locally. 
2. Add to ArcGIS pro
3. Create an MRF file from NAIP in Azure storage.
4. Add to ArcGIS Pro.

## Part 1 - ArcGIS Mosaic Datasets
1. Build a mosaic from the NAIP on Azure raster proxies.
2. Build a mosaic and add a single AWS band collection manually.
3. Build a second mosaic and add an entire path row over **your_aoi_here**
4. Introduc [MDCS](https://github.com/Esri/mdcs-py)
5. Show configuration of MDCS and resulting mosaic.

# Exercises and Homework
1. Use Optimize Rasters to take a folder of elevation data (*C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Week 4\data\data\dems*), convert to MRF, and load into Azure Storage Account.

# Github Links
  - [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
  - [MDCS](https://github.com/Esri/mdcs-py)
