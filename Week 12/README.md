# Hand Held Imagery and Motion Video
In this lecture, we will discuss and demonstrate different ways to use hand held imagery and motion video. Hand held imagery can be exploited in ArcGIS Pro and through WebApps. We will develop workflows to take imagery from hand held cameras and phones, share them to Azure sotrage or AWS S3 storage, and use the imagery in ArcGIS. We will also explore different ways to utilize full-motion video in ArcGIS Pro.

# Preparation
- Watch [Full Motion Video in Pro 2.2](https://www.esri.com/videos/watch?videoid=rGFZT9yWzRM&title=full-motion-video-in-arcgis-pro-2-2)
- Do the [Creating an Oriented Imagery Catalog in ArcGIS](https://doc.arcgis.com/en/imagery/workflows/tutorials/creating-an-oriented-imagery-catalog.htm) tutorial.

# Lecture 1 - Oriented Imagery
Using the full-motion video tools requires an **Image Analyst** license. Creating oriented imagery services and apps requires the oriented imagery add-in and oriented imagery Geoprocessing tools. Let's start bu downloadind and installing the oriented imagery add-in and oriented imagery GP tools:
  - [The Oriented Imagery Add in for ArcGIS Pro](https://www.arcgis.com/home/item.html?id=19b5028e59c141239d0a262117639f81)
  - [Oriented Imagery Management Tools for ArcGIS Pro](https://www.arcgis.com/home/item.html?id=36ee0bbedca64a5a8b68d7c69ab51728)
I have already downloaded and installed them.
1. Create a **public access level** (*Container*) ni Azure or AWS.
2. Upload photos into that public container or bucket. You can do this through the Azure or AWS webpage or you can do this using Optimize Rasters.
3. Open ArcGIS Pro. I already have the OIC Geoprocessing tools installed.
4. Add the **ManageOrientedImagery.pyt** to your Pro Project.
5. Create an **Oriented Imagery Catalog**
![]()
6. Add Images to OIC
![]()
7. Edit properties of OIC usng **Properties** GP tool. Change **MaxDistance** to **100**.
![]()
8. **Create Coverage Features**
![]()
9. **Create Coverage Map**
10. **Analyze OIC**
11. Share oriented imagery catalog to ArcGIS Online using ArcGIS Pro using **Publish OIC** GP Tool. Show that in ArcGIS Online, the **OIC** is its own item type.
12. Look at catalog in Pro using the Orineted Imagery Viewer
13. Show OIC in the WebApp.

# Lecture 2 - [Full Motion Video](https://pro.arcgis.com/en/pro-app/help/analysis/image-analyst/introduction-to-full-motion-video-in-arcgis-pro.htm)
## Drone Video
Working with Full Motion imagery has become simple. If you have **Image Analyst** licensed in ArcGIS Pro, you can just drag an image into Pro and start working with it. 

1. Open ArcGIS Pro
2. Make a connection to the folder containing the video.
3. Show that ArcGIS Pro recognizes it.
4. Drag it into the **Table of Contents**. The video player pops up and we can immediately begin working with it.
5. Hit **Play** and watch the video and tracks.
6. Hit **Pause**. **Zoom to Frame** in to show what the tracks look like.
7. Note the location of the center of the camera in each frame.
8. Let's say we want to collect the location of billboards or street signs. We can collect them in the video and the points translate to the map. FMV does a similar image space to map space conversion that we saw last week when talking about Image Coordinate Space.
9. Similarly, we can take a **Frame Snapshot**. This will put a georeferenced image on the map. How well does the image line up with the map?
10. Resume Playing. Now we are folloing the frame on the map.
11. There is a lot more functionality here. you can **Export to Powerpoint**, save the features that you collect, and create subsets of the video. I'm not going to go through all of that here. These are things you will explore in **Exercise 2** this week.

## Hand Held (iPhone) Video
The Full Motion Video capabiliites don't support every sensor, however, you can create a video that is complant with the FMV capabilities by using a processes called [**Multiplexing**](https://pro.arcgis.com/en/pro-app/tool-reference/image-analyst/video-multiplexer.htm). This is the process of combining the two files containing the video and metadata files. This can be done if the metadata is encoded in the video file by a synchronized time stamp. I am not going to go through this process here, but Esri has a [**Multiplexing Sample**](https://ps-dbs.maps.arcgis.com/home/item.html?id=6991aa3f29d64b838fb0e38b5cdb89ad) if you are interested.

I have used the [Multiplexer GP tool]() to combine image locations with the video that I have taken from an iPhone.  

When I add this to the map, you notice that the tracks follows the location. You will also notice that it doesn't have camera orientation info. I have not included that info in the nultiplexing process.


# Exercise(s)
Please somplete the following ArcGIS tutorials on Orineted Imagery and FMV:
  1. If you have not yet done the [Creating an Oriented Imagery Catalog in ArcGIS](https://doc.arcgis.com/en/imagery/workflows/tutorials/creating-an-oriented-imagery-catalog.htm) tutorial, please complete this.
  2. Complete the [FMV player tutorial.](https://doc.arcgis.com/en/imagery/workflows/tutorials/fmv-video-player-tutorial.htm)

# Homework
1. Using your iPhone, Android, or another camera that creates geotagged photots, create an orineted imagery service from some photos that you take. The photos can be of a park, a parking lot, your neighborhood; whatever you would like. You should:
  - Take the photos.
  - Upload the photos to public Azure storage or a public AWS S3 bucket.
  - Create a feature class the points to the photos in your cloud storage.
  - Share that feature class as a feature service.
**Please share the feature service with me.**
2. Take the feature service that you create in **Part 1**, and use that feature service in one of the following apps:
  - 2D App - 
  - 3D App - 
  
You can do that by appending the ?oic=**oic_item_id** to either the 2D app or 3D app urls.
**Share that link with me.**  
  
# What's Next:
- [Processing Drone Imagery Using Python - Esri Dev Summit 2019](https://www.esri.com/videos/watch?videoid=WZZG4qIj5jQ&title=Processing%20Drone%20Imagery%20using%20the%20ArcGIS%20API%20for%20Python)
- [Python Raster Types]()

# ArcGIS Drone2Map
## Videos
- [UC 2016](https://www.esri.com/videos/watch?videoid=63qAQJZGab8)
- [UC 2017](https://www.youtube.com/watch?v=T1qGsSTA_N0)
