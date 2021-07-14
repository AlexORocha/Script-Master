# IMPORTAÇÃO DAS BIBLIOTECAS E MÓDULOS ----------
import wrf
import pandas as pd
import numpy as np
import time

import plotly.figure_factory as FF
import plotly.graph_objects as go

from scipy.spatial import Delaunay
from netCDF4 import Dataset
from scipy.io import netcdf

#from utils.params import *
DICT = 'wrf_out/'
ARQ_NAME = 'wrfout_20200102.nc'
# -----------------------------------------------

#def run():

# CAPTURA DOS DADOS A PARTIR DO ARQUIVO ---------
#datain = Dataset(DICT + ARQ_NAME)
nc = netcdf.netcdf_file(DICT + ARQ_NAME, 'r')
# -----------------------------------------------

vars = nc.variables
dims = nc.dimensions
c = nc.variables['T2'].dimensions 
d = nc.variables['T2'].units 

prec = vars['RAINPROD']

print('Teste')