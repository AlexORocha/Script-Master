import xray
import numpy

DICT = 'wrf_out/'
ARQ_NAME = 'wrfout_20200102.nc'

ds = xray.open_dataset(DICT + ARQ_NAME)
ds_point = ds.sel(lon = -23.559998, lat = -46.609985)
temp = ds_point['T']
temp.plot()

temp_array = temp.values

