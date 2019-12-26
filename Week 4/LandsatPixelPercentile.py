import numpy as np
import datetime
from datetime import timedelta
import sys


import os
import pickle

debug_logs_directory = r'C:\Users\greg6750\Documents\IPython Notebooks\developing-with-imagery\Week 4\debug'

# Based on QA Band - https://landsat.usgs.gov/collectionqualityband
#QA_BAND_NUM = 7
#misc = [0, 1]
LANDSAT_4_7_CLEAR_PIX_VALS = [672, 676, 680, 684]
LANDSAT_8_CLEAR_PIX_VALS = [20480, 20484, 20512, 23552]#[2720, 2724, 2728, 2732]
LANDSAT_CLEAR_PIX_VALS = LANDSAT_4_7_CLEAR_PIX_VALS + LANDSAT_8_CLEAR_PIX_VALS
FILTER_VAL = -3001

def apply_mask(tct_stack, bqa_stack, clear_code):
    tct_stack[~np.isin(bqa_stack, clear_code)] = FILTER_VAL
    return tct_stack.astype('float')

class LandsatPixelPercentile():

    def __init__(self):
        self.name = 'Landsat Pixel Percentile'
        self.description = 'This function creates a synthetic Landsat image given a day of year range' \
            'and the percentile of the pixel that we want to calculate.'

        self.times = []
        self.predict_month = None

    def getParameterInfo(self):
        return [
            {
                'name': 'rasters',
                'dataType': 'rasters',
                'value': None,
                'required': True,
                'displayName': 'Rasters',
                'description': 'The collection of overlapping rasters to aggregate.',
            },
            {
                'name': 'sensor',
                'dataType': 'string',
                'value': 'Landsat TM',
                'required': True,
                'domain': ('Landsat TM', 'Landsat ETM', 'Landsat OLI'),
                'displayName': 'Landsat sensor to use',
                'description': 'Landsat TM, ETM, or OLI'
            },
            {
                'name': 'percentile',
                'dataType': 'numeric',
                'value': 50,
                'required': True,
                'displayName': 'Pixel Percentile',
                'description': 'Pixel Percentile (integer in range of 0 to 100)'
            },
            {
                'name': 'start_day',
                'dataType': 'numeric',
                'value': 120,
                'required': True,
                'displayName': 'Start Day of Year',
                'description': 'Start Day of Year for Pixel Filtering'
            },
            {
                'name': 'start_year',
                'dataType': 'numeric',
                'value': 2014,
                'required': True,
                'displayName': 'Start Year',
                'description': 'Start Year for Pixel Filtering'
            },
            {
                'name': 'end_day',
                'dataType': 'numeric',
                'value': 240,
                'required': True,
                'displayName': 'End Day of Year',
                'description': 'End Day of Year for Pixel Filtering'
            },
            {
                'name': 'end_year',
                'dataType': 'numeric',
                'value': 2018,
                'required': True,
                'displayName': 'End Year',
                'description': 'End Year for Pixel Filtering'
            }
        ]

    def getConfiguration(self, **scalars):
        return {
            'inheritProperties': 4 | 8,         # inherit everything but the pixel type (1) and NoData (2)
            'invalidateProperties': 2 | 4,      # invalidate histogram and statistics because we are modifying pixel values
            'inputMask': True,                  # need raster mask of all input rasters in .updatePixels().
            'resampling': False,                # process at native resolution
            'keyMetadata': ['AcquisitionDate']
        }

    def updateRasterInfo(self, **kwargs):
        #outStats = {'minimum': -1, 'maximum': 1}
        #self.outBandCount = 6

        self.times = kwargs['rasters_keyMetadata']

        self.start_day = int(kwargs['start_day'])
        self.start_year = int(kwargs['start_year'])
        self.end_day = int(kwargs['end_day'])
        self.end_year =int(kwargs['end_year'])
        self.percentile = int(kwargs['percentile'])
        self.sensor = kwargs['sensor']

        if self.sensor == 'Landsat TM' or self.sensor == 'Landsat ETM':
            self.filter = LANDSAT_4_7_CLEAR_PIX_VALS
            self.qa_band_num = 7
        elif self.sensor == 'Landsat OLI':
            self.filter = LANDSAT_8_CLEAR_PIX_VALS
            self.qa_band_num = 9
        else:
            self.filter = LANDSAT_CLEAR_PIX_VALS
            self.qa_band_num = 7

        kwargs['output_info']['pixelType'] = 'f4'  # output pixels are floating-point values
        kwargs['output_info']['histogram'] = ()  # no statistics/histogram for output raster specified
        kwargs['output_info']['statistics'] = ()  # outStatsTuple
        kwargs['output_info']['bandCount'] = self.qa_band_num - 1

        return kwargs

    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        return keyMetadata


    def updatePixels(self, tlc, shape, props, **pixelBlocks):

        fname = 'BaseDebugTemplate_{:%Y_%b_%d_%H_%M_%S}.txt'.format(datetime.datetime.now())
        filename = os.path.join(debug_logs_directory, fname)
        pickle_filename = os.path.join(debug_logs_directory, fname)

        file = open(filename, "w")
        file.write("in init.\n")

        t_vals = [j['acquisitiondate'] for j in self.times]
        pickle.dump(t_vals, open(pickle_filename[:-4] + 'pix_time.p', "wb"))

        file.write("t_vals")

        pix_blocks = pixelBlocks['rasters_pixels']
        pix_array = np.asarray(pix_blocks)
        pickle.dump(pix_blocks, open(pickle_filename[:-4] + 'pix_blocks.p', "wb"))

        file.write("pix_array")

        base_date = datetime.datetime(1900, 1, 1) - datetime.timedelta(days=2)

        file.write("base_date")

        year_doy = np.zeros((len(t_vals), 2))
        year_doy[:, 0] = [(base_date + datetime.timedelta(days=t)).year for t in t_vals]
        year_doy[:, 1] = [(base_date + datetime.timedelta(days=t)).timetuple().tm_yday for t in t_vals]

        filtered_year_doy = [[idx, ym] for idx, ym in enumerate(year_doy) if
                             ((ym[0] >= self.start_year and ym[0] <= self.end_year) and (
                                     ym[1] >= self.start_day and ym[1] <= self.end_day))]

        file.write("filtered doy")

        year_doy_filtered_indices = [idx[0] for idx in filtered_year_doy]
        pix_array_filtered = pix_array[year_doy_filtered_indices, :, :, :]

        file.write("pix_array_filered")

        pix_array_dim = pix_array_filtered.shape
        num_bands = pix_array_dim[1] - 1
        num_squares_x = pix_array_dim[2]
        num_squares_y = pix_array_dim[3]

        qa_band_ind = self.qa_band_num - 1

        file.write("qa_band_ind")

        bqa_stack = pix_array_filtered[:, qa_band_ind, :, :]

        file.write("bqa_stack")

        pix_array_filtered = pix_array_filtered[:, 0:qa_band_ind, :, :]

        file.write("pix_array_filtered")

        bqa_stack = np.expand_dims(bqa_stack, 1)
        file.write("bqa_stack")

        bqa_stack = np.repeat(bqa_stack, qa_band_ind, 1)

        pix_array_filtered = apply_mask(pix_array_filtered.astype(props['pixelType']),
                                        bqa_stack,
                                        self.filter)

        file.write("pix_array_filtered")

        masked_pix_array = np.ma.masked_where(pix_array_filtered == FILTER_VAL, pix_array_filtered)
        mdata = np.ma.filled(masked_pix_array, np.nan)

        file.write("mdata")

        percentile = np.nanpercentile(mdata,
                                      self.percentile,
                                      axis=0)

        file.write("percentile.")

        mask = np.ones((num_bands, num_squares_x, num_squares_y))

        file.write("mask")

        pixelBlocks['output_mask'] = mask.astype('u1', copy=False)
        pixelBlocks['output_pixels'] = percentile.astype(props['pixelType'], copy=False)

        file.write("done.")

        return pixelBlocks
