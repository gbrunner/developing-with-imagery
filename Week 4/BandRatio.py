import numpy as np


class BandRatio():
    def __init__(self):
        self.name = "Band Ratio Function"
        self.description = "Computes the ratio between two user defined bands."

    def getParameterInfo(self):
        return [
            {
                'name': 'raster',
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "Raster",
                'description': "The primary multi-band input raster containing red and infrared bands."
            },
            {
                'name': 'band1',
                'dataType': 'numeric',
                'value': 1,
                'required': True,
                'displayName': "Red Band Index",
                'description': "The index of the red band. The first band has index 1."
            },
            {
                'name': 'band2',
                'dataType': 'numeric',
                'value': 2,
                'required': True,
                'displayName': "Infrared Band Index",
                'description': "The index of the infrared band. The first band has index 1."
            }
        ]

    def getConfiguration(self, **scalars):
        band1 = int(scalars.get('band1', 1))
        band2 = int(scalars.get('band2', 2))

        return {
            'extractBands': (band1 - 1, band2 - 1),
            # extract only the two bands corresponding to user-specified red and infrared band indexes.
            'compositeRasters': False,  # input is a single raster, band compositing doesn't apply.
            'inheritProperties': 4 | 8,  # inherit all but the pixel type and NoData from the input raster
            'invalidateProperties': 2 | 4 | 8,
            # reset any statistics and histogram that might be held by the parent dataset (because this function modifies pixel values).
            'inputMask': False  # Don't need input raster mask in .updatePixels().
        }

    def updateRasterInfo(self, **kwargs):

        kwargs['output_info']['bandCount'] = 1  # output is a single band raster
        kwargs['output_info']['statistics'] = (
        {'minimum': -1.0, 'maximum': 1.0},)  # we know something about the stats of the outgoing NDVI raster.
        kwargs['output_info']['histogram'] = ()  # we know nothing about the histogram of the outgoing raster.
        return kwargs

    def updatePixels(self, tlc, shape, props, **pixelBlocks):
        inBlock = pixelBlocks['raster_pixels']  # get the input raster pixel block
        band1 = np.array(inBlock[0], dtype='f4')  # extractbands ensures first band is Red.
        band2 = np.array(inBlock[1], dtype='f4')  # extractbands ensures second band is Infrared

        np.seterr(divide='ignore')
        outBlock = (band2 - band1) / (band2 + band1)  # compute NDVI

        pixelBlocks['output_pixels'] = outBlock.astype(props['pixelType'])
        return pixelBlocks

    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        if bandIndex == -1:
            keyMetadata['datatype'] = 'Processed'  # outgoing raster is now 'Processed'
        elif bandIndex == 0:
            keyMetadata['wavelengthmin'] = None  # reset inapplicable band-specific key metadata
            keyMetadata['wavelengthmax'] = None
            keyMetadata['bandname'] = 'Band Ratio'
        return keyMetadata