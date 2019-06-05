# "What's Old Is New"

# Class Preparation
- Watch [How Esri Optimizes for Analytics in the Cloud](https://youtu.be/U486YxlDoeM)
- Optionally Wach Anything from [AWS Re-Invent](https://aws.amazon.com/earth/)

# Lecture
## Connecting to the Cloud
### [Landsat Path Rows](https://www.usgs.gov/land-resources/nli/landsat/landsat-shapefiles-and-kml-files)

### Connect to Landsat 8 on AWS using [Cloud Store Connection](https://pro.arcgis.com/en/pro-app/help/projects/connect-to-cloud-stores.htm)
  - Using AWS S3 COnnection
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
### What Else?
- Processing Functions applied to imagery.
- Download locally?
- Mosaic from local download.
- Sqgue into next week to mosaic against data in S3


# Datasets
- [Landsat-8 Public Bucket](https://registry.opendata.aws/landsat-8/)
  - https://landsatonaws.com/
- [NAIP is Requester Pays](https://registry.opendata.aws/naip/)
- [USGS Lidar is Requester Pays](https://registry.opendata.aws/usgs-lidar/)
- [Sentinel-2](https://registry.opendata.aws/sentinel-2/)

# Links
- [Earth on AWS - Datasets](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)
