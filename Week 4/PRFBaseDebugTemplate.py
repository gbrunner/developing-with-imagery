import numpy as np
import datetime

import os
import pickle

debug_logs_directory = r'C:\PROJECTS\SFA\debug'

class PRFBaseDebugTemplate:

    def __init__(self):
        self.name = 'Template to use to get into the pixel blocks'
        self.description = 'This is a raster function that you can use to get into the pixel blocks.'


    def getParameterInfo(self):
        return [
            {
                'name': 'raster',
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': 'Raster',
                'description': 'A Single Input Raster.',
            }
        ]

    def getConfiguration(self, **scalars):
        return {
            'inheritProperties': 1 | 2 | 4 | 8,
        }

    def updateRasterInfo(self, **kwargs):
        return kwargs

    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        return keyMetadata

    def updatePixels(self, tlc, shape, props, **pixelBlocks):

        fname = 'singleDataset_{:%Y_%b_%d_%H_%M_%S}.txt'.format(datetime.datetime.now())
        filename = os.path.join(debug_logs_directory, fname)
        pickle_filename = os.path.join(debug_logs_directory, fname)

        ## Using Print Statements
        #file = open(filename, "w")
        #file.write("in init.\n")

        pix_blocks = pixelBlocks['raster_pixels']
        pix_array = np.asarray(pix_blocks)

        pickle.dump(pix_blocks, open(pickle_filename[:-4] + 'pix_blocks.p', "wb"))

        pix_array_dim = pix_array.shape
        mask = np.ones(pix_array_dim)

        pixelBlocks['output_pixels'] = mask.astype(props['pixelType'], copy=False)

        #file.write("DONE.")
        #file.close()

        return pixelBlocks
