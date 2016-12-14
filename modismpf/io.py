'''
Methods and wrappers to serve data to MODIS melt pond fraction
calculation methods
'''

import numpy as np

def get_dummy_bands(shape=(10,10)):
    '''
    Return three dummy NaN bands
    Keyword arguments:

      shape (tuple) : shape of each of the output bands

    Returns:

        band_[1,2,3]: (numpy.ndarray) Numpy arrays with NaN values
    '''
    nan_band = np.ones(shape) * np.nan
    [band_1, band_2, band_3] = [nan_band for _ in range(3)]
    return band_1, band_2, band_3
