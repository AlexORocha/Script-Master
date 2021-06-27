import netCDF4 as nc
import numpy as np

DICT = 'wrf_out/'
ARQ_NAME = 'wrfout_20200102.nc'

nc_file = nc.Dataset(DICT + ARQ_NAME)

T = nc_file['Times'][:]
P = nc_file['PB'][:]


print(nc_file)
