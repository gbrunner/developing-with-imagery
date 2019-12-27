# [Image Coordinate Space](https://pro.arcgis.com/en/pro-app/help/analysis/image-analyst/what-is-image-space-analysis-.htm)
When a sensor collects a picture and forms an image, it captures the scene in perspective geometry. As a result, the image has its own unique mapping of the 3D world into that specific 2D image. For remotely sensed images, this geometry is described in a sensor model that accompanies the image in the metadata. The perspective mode of the map view display provides the capability to display oblique imagery in an image coordinate system, called image space, rather than a map coordinate system to enable more intuitive image interpretation. In this lecture, we will learn about image coordinate space. We will learn how to change from viewing in map space to image coordinate space in ArcGIS Pro and Excalibur, we will understand how to measure features in image coordinate space, and we will go behind the scenes to understand how ArcGIS renders an image in image coordinate space by using the ArcGIS API for Python.

# Preparation
- [Visualizing and Editing Data in Image Coordinate Space](https://www.esri.com/videos/watch?videoid=kObjN4KOYqQ&title=visualizing-and-editing-data-in-image-coordinate-space)
- [ArcGIS Excalibur: Experience the Value and Power of Imagery through the WebGIS Pattern](https://www.esri.com/videos/watch?videoid=wtAFXG-sG7g&title=arcgis-excalibur-experience-the-value-and-power-of-imagery-through-the-webgis-pattern)

# Lecture 1 - Image Coordinate Space in ArcGIS Pro
Review geographic coordinates space,projected coordinate space, and image coordinate space (ICS_Background.pptx).

## Using Individual Rasters
1. Make a folder connection to Georgia image folder.
2. Add a **PAN.IMD** image to a new map.
3. Select **Llist by Perspective Imagery**
4. Set single image as **Focus Image**
  - See the metadata dropdown on the map?
  - Notice how the map get reoriented?
5. Show that you can **Rotate** it to **Up** or **North** on the **Appearance** ribbon.
6. Show **Mensuration**capabilities on **Imagery** tab.
7. Show and compare results from **Base to Top Height** and **Base to Top Shadow Height**. 


## Using a Mosaic Dataset
Built mosaic using **Wolrd-View 2** raster type using **Panchromatic** processing template.Notice that the mosaic dataset doesn't get added to the **Focusable Images**.
1. Add mosaic to map.
2. Right click on mosaic dataset.
3. Got to **Selection->Explore Raster Items**
4. **Zoom To** item.
5. Look at the raster functions.
6. Go to **Select** tab.
7. **Add Item** to current map
8. Notice that the tool adds the selcted item to the **Focusable Images**
9. You can now treat this like an individual raster in image space.

## Using an Image Service
Image Services
- https://imageserver.imagery.esri.com/arcgis/rest/services/Maxar/SanFrancisco_WV3_PS_DEM/ImageServer
- https://imageserver.imagery.esri.com/arcgis/rest/services/Applanix/West_Coast_Oblique_10mDEM_Applanix/ImageServer

Add one of these image services to the map. Show that you can work in image space similar to how you did with  a mosaic dataset.

# Lecture 2 - Image Coordinate Space in Excalibur
## Segue from Image Service into Excalibur
Will Excalibur be in ArcGIS Online? Is it just Portal?

# Lecture 3 - Image Coordinate Space in Python
Image space and the ICS re exposed through the service REST endpoints. For insight into what this looks like, let's take a look at the rest endpoints and let's see what those look like through the ArcGIS API for Python.

We can also use Python to render the images in these different coordinate spaces. 
- WV3_ImageSpace_in_Jupyter.ipynb
- Applanix_ImageSpace_in_Jupyter.ipynb

# Excercise and Homework
1. Complete the following exercise: [Use image space analysis to work with oblique imagery](https://pro.arcgis.com/en/pro-app/help/analysis/image-analyst/using-image-space-analysis-to-work-with-oblique-imagery.htm)
2. Using the Atlanta, Vegas, or Paris imagery, find and measure the heights of several of the tallest building in the respective cities.
3. **If we have Excalibur** Create a Mosaic Dataset from the Atlanta, Vegas, or Paris imagery. The mosaics should contain at least 2 images. Be sure to select the right **raster type** and **processing template**. Publish the mosaic dataset to your image server. Create an **Excalibur Project** to consume the image service.
4. **Challenge** Write a Python function that converts a point from geographic space and converts it to ICS. Show that you can use Python and plot that point on top of the same image in ICS and GCS.


