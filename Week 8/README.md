# Advanced Imagery Analysis
## Scientific Analysis
### Data Cubes in Pro

## Deep Learning and AI

### Lecture
- [Deep Learning in ArcGIS Storymap](https://www.arcgis.com/apps/Cascade/index.html?appid=3723542905dd41c4b05831443459286e)

### Lesson - [Using Deep Learning to Assess Palm Tree Health](https://learn.arcgis.com/en/projects/use-deep-learning-to-assess-palm-tree-health/)
1. Install [TensorFlow](https://pro.arcgis.com/en/pro-app/tool-reference/image-analyst/set-up-tensorflow-deep-learning-framework-for-arcgis.htm#ESRI_SECTION1_C30D73392D964D51A8B606128A8A6E8F)
2. Create Training Samples(https://learn.arcgis.com/en/projects/use-deep-learning-to-assess-palm-tree-health/lessons/create-training-samples.htm)
3. [Detect Palm Trees](https://learn.arcgis.com/en/projects/use-deep-learning-to-assess-palm-tree-health/lessons/detect-palm-trees-with-a-deep-learning-model.htm)
4. [Estimate Palm Tree Health](https://learn.arcgis.com/en/projects/use-deep-learning-to-assess-palm-tree-health/lessons/estimate-vegetation-health.htm)

### Assignment - Detecting Objects Using the [xView](http://xviewdataset.org/) TensorFlow Model
#### Read the following
- [What is xView?](http://xviewdataset.org/)
- [Getting Started with xView](https://medium.com/@dariusl/getting-started-with-the-diux-xview-dataset-for-overhead-object-detection-84fc4d918d09)
- [xView Baseline Results](https://medium.com/picterra/the-xview-dataset-and-baseline-results-5ab4a1d0f47f)
 
#### Objective
The objective of this Assignment is to test how accurately the xView model detects objects around Khartoum International Airport in Sudan and Hatfield International Airport in Atlanta. You can learn more about these datasets here: https://spacenetchallenge.github.io/.

1. Khartoum Airport: Run the deep learning model using Detect Objects Using Deep Learning using the multires.pd model. Note that

2. Hatfield Airport: Run the deep learning model using Detect Objects Using Deep Learning using the multires.pd model. In order for this to work, you will have to process the Hatfield Airport images into a 30 cm pixel pansharped RGB image with pixels that scale from 0 to 255. Create a raster function chain to process the PAN and MS images into a 30 cm pixel image that will work with the multires.pb model. That function chain will look something like:

Extract Bands Function -> Pansharpen Function -> Resample Function -> Stretch Function

**Helpful Hint:** If you are having trouble, first try detecting objects in the **Validation Dataset**.

## Helpful Links
- https://spacenetchallenge.github.io/
- ```aws s3 ls s3://spacenet-dataset/```
- [GeoAI](https://medium.com/geoai)
