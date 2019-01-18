# enterprise-imagery-management-dissemination-analysis
Repo for develping materials for a class in Enterprise Imagery Management, Dissemination, and Analysis

## Instructor Information
Instructor:	Gregory Brunner  
Email Address:	gbrunner@esri.com  
Office Hours:	By request  

## Description
You know what NDVI means. You have already learned what SAR is and how to use it. You even know a little bit or raster algebra. What you really want to know, however, is *how does Esri create and maintain their [global Landast service](https://aws.amazon.com/earth/)?*  *How do I use Python to interface with ArcGIS Image Services?* *What can I do with drone imagery?*  In **Enterprise Imagery Management, Dissemination, and Analysis**, you will learn how to create global imagery mosaics, write and implement advanced imagery analysis algorithms, apply these analytical methods at scale using AWS and raster Analyics. You will also learn techniques for processing and analysing imagery collected by drones and other highly oblique imagery datasets.

## Course Objectives

## Textbooks
None

## Prerequisites
- Intro to GIS (using ArcGIS Pro)
- Programming with Python
- An ArcGIS Server\Enterprise Course
- Classical Remote Sensing

## Textbooks

## Course Schedule
| Week    | Topics | Date |
|---------|--------| ---- |
| 1    | Imagery in ArcGIS Pro|
| 2    | Mosaic Datasets (in ArcGIS Pro) |
| 3    | Raster Processing with Python\Numpy (more traditional method) |
| 4    | Python Raster Functions (Paradigm for analysis at scale) |
| 5    | Rasters in S3 - Optimize Rasters|
| 6    | Using Imagery in ArcGIS Online |
| 7    | Image Server Deployment |
| 8    | Image Server - Image Services |
| 9    | Image Server Use - Raster Analytics |
| 10   | Advanced Raster Analytics - Algorithms (Scientific Analysis and Machine Learning) |
| ~~10~~   |~~Advanced Methods - Leveraging AWS for Automation~~ |
| 11   | Using Imagery with the ArcGIS API for Javascript |
| 12   | Using Imagery with the ArcGIS API for Python |
| 13   | Advanced Methods with the ArcGIS API for Python |
| 14   | Special Topics: Drone Mapping (Drone2Map) |
| 15   | Special Topics: Ortho Mapping (ArcGIS Pro) and Ortho Maker (Server) |

## Structure of the Course
- Weeks 1 - 5: Desktop
- Weeks 6 - 10: Server & Cloud
- Weeks 11 - 13: Using Imagery through Esri WebGIS APIs (Python and Javascript)
- Weeks 14, 15: Creating Imagery Products

### Week 1
Imagery in ArcGIS Pro
- Geoprocessing vs. Raster Functions
- Working with individual rasters, file in, file out
- Raster and remote sensing formats:
  - TIFF
  - Landsat
  - DEM
  - LiDAR\LAS
  
### Week 2
- Intro to mosaic datasets
- Landsat Mosaic
- DEM Mosaic
- Lidar Mosaic
- Talk about other file formats

### Week 3
- Raster Processing with Numpy
- Also show Raster proccessig using Raster Algebra and Python if necessary.

### Week 4
Python Raster Functions
- [2018  presentation](https://www.youtube.com/watch?v=XBMZfjGn_UY)
- [2017 Presentation](https://www.youtube.com/watch?v=OgwnKRrVHN0)

### Week 5
- [Optimize Rasters](https://github.com/Esri/OptimizeRasters/)
- download 8 jp2\jpeg\tiff images 
- ~~convert to MRF locally~~
- copy to S3
- create local raster proxy files using [Optimize Rasters](https://github.com/Esri/OptimizeRasters/)
- add to mosaic in PostgreSQL
- publish as image service

### Week 6
Using Imagery in ArcGIS Online will bridget the gap between Desktop and Server\Cloud. We will juxtoapose traditional workflows in ArcGIS Pro vs. those same workflows through ArcGIS Online. This will lay the framework for the next 9 weeks.

Chapter 9 of Pinde Fu's [**Getting to Know WebGIS**](https://esripress.esri.com/storage/esripress/images/353/gtkwebgis_third_toc.pdf)


