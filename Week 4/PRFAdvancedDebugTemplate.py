import numpy as np
import datetime

import os
import pickle

debug_logs_directory = r'C:\PROJECTS\SFA\debug'

class PRFAdvancedDebugTemplate:

    def __init__(self):
        self.name = 'Template to use to get into the pixel blocks'
        self.description = 'This is a raster function that you can use to get into the pixel blocks.'

        # If you want to get time data or other metadata.
        self.times = []

    def getParameterInfo(self):
        return [
            {
                'name': 'rasters',
                'dataType': 'rasters',
                'value': None,
                'required': True,
                'displayName': 'Rasters',
                'description': 'The collection of overlapping rasters to aggregate.',
            }
        ]

    def getConfiguration(self, **scalars):
        return {
            'inheritProperties': 1 | 2 | 4 | 8,  # 1 | 2 |  inherit everything but the pixel type (1) and NoData (2)
            'keyMetadata': ['acquisitiondate', 'instrument', 'level']
        }

    def updateRasterInfo(self, **kwargs):

        self.times = kwargs['rasters_keyMetadata']

        return kwargs

    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        return keyMetadata

    def updatePixels(self, tlc, shape, props, **pixelBlocks):

        fname = 'updatePixels_{:%Y_%b_%d_%H_%M_%S}.txt'.format(datetime.datetime.now())
        filename = os.path.join(debug_logs_directory, fname)
        pickle_filename = os.path.join(debug_logs_directory, fname)

        ## Using Print Statements
        #file = open(filename, "w")
        #file.write("in init.\n")

        t_vals = self.times
        pickle.dump(t_vals, open(pickle_filename[:-4] + 'pix_time.p', "wb"))

        pix_blocks = pixelBlocks['rasters_pixels']
        pix_array = np.asarray(pix_blocks)

        pickle.dump(pix_blocks, open(pickle_filename[:-4] + 'pix_blocks.p', "wb"))

        pix_array_dim = pix_array.shape
        mask = np.ones(pix_array_dim[1:])

        pixelBlocks['output_pixels'] = mask.astype(props['pixelType'], copy=False)

        #file.write("DONE.")
        #file.close()

        return pixelBlocks
