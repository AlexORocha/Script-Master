import numpy as np
from netCDF4 import Dataset
import pandas as pd

f = Dataset('wrf_out/wrfout_20200102.nc', mode='r')
long = -23.559998
lat = -46.609985

cor_lat = pd.DataFrame(f.variables['XLAT'][0][:])
cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - lat)})
a = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]

cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])
cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - long)})
b = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]

vlr = (f.variables['T2'][ : , a , b ] - 273.15)[0]

vlr