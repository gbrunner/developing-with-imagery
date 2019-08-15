# "What's Old Is New"

# Preparation
1. Read:
    - [Managing Imagery in the Cloud](http://proceedings.esri.com/library/userconf/proc17/tech-workshops/tw_630-625.pdf)
    - [MRF](https://community.esri.com/thread/212729-mrf-s3-mosaics-caches-and-optimization)
    - [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
    - [MDCS](https://github.com/Esri/mdcs-py)
2. Watch:
    - [Optimize Rasters](https://www.youtube.com/watch?v=NEu0BYA1jAA)

# Lecture - Interfacing with imagery in Azure, AWS, and Google Cloud
## Part 1 - ArcGIS Mosaic Datasets
1. Build a mosaic from the NAIP on Azure raster proxies.
2. Build a mosaic and add a single AWS band collection manually.
3. Build a second mosaic and add an entire path row over **your_aoi_here**
4. Introduc [MDCS](https://github.com/Esri/mdcs-py)
5. Show configuration of MDCS and resulting mosaic.

## Part 2 - Interfacing with the same imagery through GDAL and rasterio

### [GDAL](https://pypi.org/project/GDAL/) and Python
1. Already installed in ArcGIS Pro's Conda environment

### [rasterio](https://rasterio.readthedocs.io/en/stable/) and Python
**Rasterio** is a Python wrapper around *GDAL* that is used specifically for working with raster (imagery) data.

1. Install ```rasterio``` and ```boto3``` into **arcgispro-py3-clone** environment
  - ```conda install boto3```
  - ```conda install -c conda-forge rasterio```. For instructions, go to [```conda install rasterio```](https://github.com/conda-forge/rasterio-feedstock)
2. **Exercise:** [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)

# Github Links
  - [Optimize Rasters](https://github.com/Esri/OptimizeRasters)
  - [MDCS](https://github.com/Esri/mdcs-py)
