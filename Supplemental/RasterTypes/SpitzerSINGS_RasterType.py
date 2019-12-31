import os
import re
import arcpy
# import glob
# import csv
from datetime import datetime
from dateutil import tz

meta_data_dict ={
   'DDO053':{
      'OBJECT':'DDO053',
      'DATE':'2007-03-27T16:28:43',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'DDO154':{
      'OBJECT':'DDO154',
      'DATE':'2007-03-27T16:36:03',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'DDO165':{
      'OBJECT':'DDO165',
      'DATE':'2007-03-27T16:31:52',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'HoII':{
      'OBJECT':'HoII',
      'DATE':'2007-03-27T18:59:11',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3031':{
      'OBJECT':'NGC3031',
      'DATE':'2007-03-28T08:46:59',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'HoI':{
      'OBJECT':'HoI',
      'DATE':'2007-04-04T20:53:35',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'ic2574':{
      'OBJECT':'ic2574',
      'DATE':'2007-03-27T21:03:35',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'IC 4710':{
      'OBJECT':'IC 4710',
      'DATE':'2007-03-27T18:00:44',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'M81DwA':{
      'OBJECT':'M81DwA',
      'DATE':'2007-03-27T17:56:41',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'M81DwB':{
      'OBJECT':'M81DwB',
      'DATE':'2007-03-31T00:07:21',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'Mrk33':{
      'OBJECT':'Mrk33',
      'DATE':'2007-03-27T17:59:40',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC0024':{
      'OBJECT':'NGC0024',
      'DATE':'2007-04-05T05:16:00',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC0337':{
      'OBJECT':'NGC0337',
      'DATE':'2007-03-27T18:14:41',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC0584':{
      'OBJECT':'NGC0584',
      'DATE':'2007-03-27T18:16:01',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC628':{
      'OBJECT':'NGC628',
      'DATE':'2007-03-27T19:07:50',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC0855':{
      'OBJECT':'NGC0855',
      'DATE':'2007-03-27T18:12:36',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC0925':{
      'OBJECT':'NGC0925',
      'DATE':'2007-03-27T20:45:06',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1097':{
      'OBJECT':'NGC1097',
      'DATE':'2007-03-27T19:40:59',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1266':{
      'OBJECT':'NGC1266',
      'DATE':'2007-03-28T13:29:31',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1291':{
      'OBJECT':'NGC1291',
      'DATE':'2007-03-28T17:06:32',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1316':{
      'OBJECT':'NGC1316',
      'DATE':'2007-03-28T16:52:40',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1377':{
      'OBJECT':'NGC1377',
      'DATE':'2007-03-27T22:50:48',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1404':{
      'OBJECT':'NGC1404',
      'DATE':'2007-03-28T03:15:55',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1482':{
      'OBJECT':'NGC1482',
      'DATE':'2007-03-27T22:45:20',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1512':{
      'OBJECT':'NGC1512',
      'DATE':'2007-03-28T01:04:58',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1566':{
      'OBJECT':'NGC1566',
      'DATE':'2007-03-28T01:26:24',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC1705':{
      'OBJECT':'NGC1705',
      'DATE':'2007-03-27T23:10:34',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC2403':{
      'OBJECT':'NGC2403',
      'DATE':'2007-03-28T07:10:50',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC2798 offset':{
      'OBJECT':'NGC2798 offset',
      'DATE':'2007-03-27T22:08:05',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC2841':{
      'OBJECT':'NGC2841',
      'DATE':'2007-04-05T20:24:58',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC2915':{
      'OBJECT':'NGC2915',
      'DATE':'2007-04-03T17:30:26',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC2976':{
      'OBJECT':'NGC2976',
      'DATE':'2007-03-27T19:18:13',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3034':{
      'OBJECT':'NGC3034',
      'DATE':'2007-04-05T15:20:41',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3049':{
      'OBJECT':'NGC3049',
      'DATE':'2007-03-27T18:16:40',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3184':{
      'OBJECT':'NGC3184',
      'DATE':'2007-04-05T13:53:46',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3190':{
      'OBJECT':'NGC3190',
      'DATE':'2007-03-27T20:02:50',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3198':{
      'OBJECT':'NGC3198',
      'DATE':'2007-03-27T18:43:10',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3265':{
      'OBJECT':'NGC3265',
      'DATE':'2007-03-27T14:15:13',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3351':{
      'OBJECT':'NGC3351',
      'DATE':'2007-03-27T15:34:16',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3521':{
      'OBJECT':'NGC3521',
      'DATE':'2007-03-27T16:20:25',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3621':{
      'OBJECT':'NGC3621',
      'DATE':'2007-04-06T03:11:51',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3627':{
      'OBJECT':'NGC3627',
      'DATE':'2007-03-27T16:43:40',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3773':{
      'OBJECT':'NGC3773',
      'DATE':'2007-03-27T14:05:45',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC3938':{
      'OBJECT':'NGC3938',
      'DATE':'2007-03-27T16:11:27',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4125':{
      'OBJECT':'NGC4125',
      'DATE':'2007-03-27T16:50:21',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4236':{
      'OBJECT':'NGC4236',
      'DATE':'2007-03-27T20:35:58',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4254':{
      'OBJECT':'NGC4254',
      'DATE':'2007-03-27T15:00:17',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4321':{
      'OBJECT':'NGC4321',
      'DATE':'2007-03-26T23:14:59',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4450':{
      'OBJECT':'NGC4450',
      'DATE':'2007-03-26T22:29:11',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4536':{
      'OBJECT':'NGC4536',
      'DATE':'2007-04-04T15:39:47',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4552':{
      'OBJECT':'NGC4552',
      'DATE':'2007-03-26T23:23:08',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4559':{
      'OBJECT':'NGC4559',
      'DATE':'2007-03-27T00:04:02',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4569':{
      'OBJECT':'NGC4569',
      'DATE':'2007-03-26T21:59:45',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4579':{
      'OBJECT':'NGC4579',
      'DATE':'2007-03-26T20:57:59',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4594':{
      'OBJECT':'NGC4594',
      'DATE':'2007-03-26T16:54:15',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4625':{
      'OBJECT':'NGC4625',
      'DATE':'2007-04-06T05:33:02',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4631':{
      'OBJECT':'NGC4631',
      'DATE':'2007-04-04T18:28:22',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4725':{
      'OBJECT':'NGC4725',
      'DATE':'2007-03-26T18:09:26',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4736':{
      'OBJECT':'NGC4736',
      'DATE':'2007-03-26T23:52:29',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC4826':{
      'OBJECT':'NGC4826',
      'DATE':'2007-03-26T17:43:49',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5033':{
      'OBJECT':'NGC5033',
      'DATE':'2007-03-26T19:45:38',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5055':{
      'OBJECT':'NGC5055',
      'DATE':'2007-03-23T21:18:04',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5194_95':{
      'OBJECT':'NGC5194_95',
      'DATE':'2007-03-30T05:12:24',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5408':{
      'OBJECT':'NGC5408',
      'DATE':'2007-03-23T19:06:56',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5474':{
      'OBJECT':'NGC5474',
      'DATE':'2007-04-05T18:37:23',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5713':{
      'OBJECT':'NGC5713',
      'DATE':'2007-03-23T16:57:45',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC5866':{
      'OBJECT':'NGC5866',
      'DATE':'2007-03-23T19:32:11',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC6822':{
      'OBJECT':'NGC6822',
      'DATE':'2007-04-04T21:27:04',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC6946':{
      'OBJECT':'NGC6946',
      'DATE':'2007-04-05T17:04:46',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC7331':{
      'OBJECT':'NGC7331',
      'DATE':'2007-03-30T14:26:00',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC7552':{
      'OBJECT':'NGC7552',
      'DATE':'2007-03-23T15:45:03',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'NGC7793':{
      'OBJECT':'NGC7793',
      'DATE':'2007-03-23T17:13:45',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   },
   'Tol89':{
      'OBJECT':'Tol89',
      'DATE':'2007-04-05T20:56:55',
      'TELESCOP':'Spitzer',
      'INSTRUME':'IRAC',
      'CREATOR':'S14.0.0',
      'ORIGIN':'NOAO-IRAF FITS Image Kernel July 2003'
   }
}

class DataSourceType():
    Unknown = 0
    File = 1
    Folder = 2

class RasterTypeFactory:

    def getRasterTypesInfo(self):
        self.object_auxField = arcpy.Field()
        self.object_auxField.name = 'Object'
        self.object_auxField.aliasName = 'Module'
        self.object_auxField.type = 'String'
        self.object_auxField.length = 20

        self.telescope_auxField = arcpy.Field()
        self.telescope_auxField.name = 'Telescope'
        self.telescope_auxField.aliasName = 'Observation Type'
        self.telescope_auxField.type = 'String'
        self.telescope_auxField.length = 20

        self.date_auxField = arcpy.Field()
        self.date_auxField.name = 'Date'
        self.date_auxField.aliasName = 'Date'
        self.date_auxField.type = 'Date'
        self.date_auxField.length = 50

        self.instrument_auxField = arcpy.Field()
        self.instrument_auxField.name = 'Instrument'
        self.instrument_auxField.aliasName = 'Instrument'
        self.instrument_auxField.type = 'Text'
        self.instrument_auxField.length = 20

        self.creator_auxField = arcpy.Field()
        self.creator_auxField.name = 'Creator'
        self.creator_auxField.aliasName = 'Creator'
        self.creator_auxField.type = 'Text'
        self.creator_auxField.length = 20

        self.origin_auxField = arcpy.Field()
        self.origin_auxField.name = 'Origin'
        self.origin_auxField.aliasName = 'Origin'
        self.origin_auxField.type = 'Text'
        self.origin_auxField.length = 50

        return [
            {
                'rasterTypeName': 'SINGS',
                'builderName': 'SINGSBuilder',
                'description': ("Supports Spitzer Space Telescop SINGS Data."),
                'supportsOrthorectification': False,
                'enableClipToFootprint': True,
                'isRasterProduct': True,
                'dataSourceType': (DataSourceType.File | DataSourceType.Folder),
                'dataSourceFilter': '*.tif',
                # 'supportedUriFilters': [
                #    {
                #        'name': 'Levels',
                #        'allowedProducts':'Res01',
                #        'supportsOrthorectification': False,
                #        'supportedTemplates': 'Res01'
                #    }
                # ],
                'processingTemplates': [
                    {
                        'name': 'SINGS_Default',
                        'enabled': False,
                        'outputDatasetTag': 'Thematic',
                        'primaryInputDatasetTag': 'Thematic',
                        'isProductTemplate': False,
                        'functionTemplate': 'SINGS_Default.rft.xml'
                    }
                ],
                'bandProperties': [
                    {
                        'bandName': 'IRAC 1',
                        'bandIndex': 1,
                        'datasetTag': 'Spiter IRAC'
                    },
                    {
                        'bandName': 'IRAC 2',
                        'bandIndex': 2,
                        'datasetTag': 'Spiter IRAC'
                    },
                    {
                        'bandName': 'IRAC 3',
                        'bandIndex': 3,
                        'datasetTag': 'Spiter IRAC'
                    },
                    {
                        'bandName': 'IRAC 4',
                        'bandIndex': 4,
                        'datasetTag': 'Spiter IRAC'
                    }
                ],
                'fields': [self.object_auxField,
                           self.telescope_auxField,
                           self.date_auxField,
                           self.instrument_auxField,
                           self.creator_auxField,
                           self.origin_auxField]
            }
        ]


# ----- ## ----- ## ----- ## ----- ## ----- ## ----- ## ----- ## ----- ##
# S2Builder builder class
# ----- ## ----- ## ----- ## ----- ## ----- ## ----- ## ----- ## ----- ##


class SINGSBuilder():

    def __init__(self, **kwargs):
        self.SensorName = 'Spitzer Space Telescope - IRAC'

    def build(self, itemURI):
        # Make sure that the itemURI dictionary contains items
        print(itemURI)

        arcpy.AddMessage(itemURI)
        if len(itemURI) <= 0:
            return None

        try:
            # print('HERE')
            # ItemURI dictionary passed from crawler containing
            # path, tag, display name, group name, product type
            path = None
            if 'path' in itemURI:
                path, filename = os.path.split(itemURI['path'])
                rasterPath = itemURI['path']
            else:
                path, filename = os.path.split(itemURI)
                rasterPath = itemURI

            for key in meta_data_dict:
                # print(key)
                if key.lower() in filename:
                    image_item = meta_data_dict[key]

            metadata = {}

            metadata['object'] = image_item['OBJECT']
            metadata['date'] = image_item['DATE']
            metadata['telescope'] = image_item['TELESCOP']
            metadata['instrument'] = image_item['INSTRUME']
            metadata['creator'] = image_item['CREATOR']
            metadata['origin'] = image_item['ORIGIN']

            # define a dictionary of variables
            variables = {}
            variables['DefaultMaximumInput'] = 10000
            variables['DefaultGamma'] = 0

            # Assemble everything into an outgoing dictionary
            # Changed order of files. Now in ascending pixel size (BGRN, RESW, CAW, SCL) // AP 2018-11-15
            builtItem = {}
            builtItem['keyProperties'] = metadata
            builtItem['itemUri'] = rasterPath

            builtItem['raster'] = {'uri': itemURI['path']}
            # {'functionDataset':
            # {'rasterFunction': 'GAEZ_Res01_Default.rft.xml',
            #  'rasterFunctionArguments': {
            #      'Raster1': rasterPath
            #      }
            #  }
            # }

            builtItemsList = list()
            builtItemsList.append(builtItem)

            # import datetime
            #debug_logs_directory = r'C:\PROJECTS\SINGS'
            #fname = '{:%Y_%b_%d_%H_%M_%S}_t.txt'.format(datetime.datetime.now())
            #filename = os.path.join(debug_logs_directory, fname)

            #file = open(filename,"w")
            #file.write(str(builtItemsList))
            #file.close()

            return builtItemsList

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return None
