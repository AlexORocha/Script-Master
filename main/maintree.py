# IMPORTAÇÃO DAS BIBLIOTECAS --------------------
import wrf
from scipy.io import netcdf
import matplotlib.pyplot as plt
import numpy as np
# -----------------------------------------------

# CONSTANTES ------------------------------------
barb_size = 3
windmax = 30
windmin = 0
#------------------------------------------------

# DIRETÓRIOS ------------------------------------
DICT = 'wrf_out/'
ARQ_NAME = 'wrfout_20200102.nc'
# -----------------------------------------------

nc = netcdf.netcdf_file(DICT + ARQ_NAME, 'r') # ABRIR O ARQUIVO E ATRIBUIR AO OBJETO 'nc'

T = wrf.getvar(nc, "Times",timeidx=wrf.ALL_TIMES, method="cat") # CAPTURA OS DADOS DE TIME
T = np.array(T) # TRANSFORMA EM ARRAY



#u = wrf.getvar(nc, "U", timeidx=wrf.ALL_TIMES, method="cat") #Componente zonal do vento
#v = wrf.getvar(nc,"V", timeidx=wrf.ALL_TIMES, method="cat")  #Comonente meridional do vento



Theta = wrf.getvar(nc, "TH2", timeidx=wrf.ALL_TIMES, method="cat")
#um_espc = wrf.getvar(nc, "",timeidx=wrf.ALL_TIMES, method="cat")

Temp = wrf.getvar(nc, "T", timeidx=wrf.ALL_TIMES, method="cat")
Temps = []

for i in range(25):
    Temps.append(Temp[i][0][0][0])



print(Temps)

#for Temperatura in Temperaturas:    
#    temperatura_media = 


P = wrf.getvar(nc, "PB", timeidx=wrf.ALL_TIMES, method="cat")

LON = wrf.getvar(nc,"XLONG", timeidx=wrf.ALL_TIMES, method="cat")#[0][0][0] #Longitude
LAT = wrf.getvar(nc,"XLAT", timeidx=wrf.ALL_TIMES, method="cat")#[0][0][0]   #Latitude

#REL_UM = wrf.getvar(nc, "RH", timeidx=wrf.ALL_TIMES, method="cat")
#ALT_CM = wrf.getvar(nc, "", timeidx=wrf.ALL_TIMES, method="cat")

#PREC = wrf.getvar(nc, "", timeidx=wrf.ALL_TIMES, method="cat")

proj = plt.figure(figsize=(8,12))
proj = plt.plot(T, Temps)
proj = plt.title('Previsão do BRAMS para Antofagasta, CHL')
plt.show()

print('Teste')
