from scipy.io import netcdf
from utils.params import DICT, ARQ_NAME
import wrf

# FUNÇÃO PARA ABRIR O ARQUIVO
def getvars():
    nc = netcdf.netcdf_file(DICT + ARQ_NAME, 'r') # ABRIR O ARQUIVO E ATRIBUIR AO OBJETO 'nc'
    return nc


# FUNÇÃO PARA RETORNAR O TEMPO
def measTime(nc):
    Time = wrf.getvar(nc,"Times", timeidx=wrf.ALL_TIMES, method="cat")
    return Time


# FUNÇÃO PARA RETURNAR U E V
def winds(nc):
    u = wrf.getvar(nc,"U", timeidx=wrf.ALL_TIMES, method="cat")
    v = wrf.getvar(nc,"V", timeidx=wrf.ALL_TIMES, method="cat")

    return u, v


# FUNÇÃO PARA RETORNAR A LATITUDE
def getlatlong(nc):
    Lat = wrf.getvar(nc,"XLAT", timeidx=wrf.ALL_TIMES, method="cat")[0][0][0]
    Long = wrf.getvar(nc,"XLONG", timeidx=wrf.ALL_TIMES, method="cat")[0][0][0]

    return Lat, Long

# FUNÇÃO PARA RETORNAR AS TEMPERATURAS
def temperature(nc):
    Temp = wrf.getvar(nc, "T", timeidx=wrf.ALL_TIMES, method="cat")
    Temps = []

    for i in range(25):
        Temps.append(Temp[i][0][0][0])

    return Temps


# FUNÇÃO PARA RETORNAR AS PRESSÕES
def pressure(nc):
    Pres = wrf.getvar(nc, "PSFC", timeidx=wrf.ALL_TIMES, method="cat")
    Press = []

    for i in range(25):
        Press.append(Pres[i][0][0]/100)

    return Press


# FUNÇÃO PARA RETORNAR AS TEMPERATURAS POTENCIAIS
def potTemp(nc):
    Theta = wrf.getvar(nc, "TH2", timeidx=wrf.ALL_TIMES, method="cat")
    Thetas = []

    for i in range(25):
        Thetas.append(Theta[i][0][0])

    return Theta


# FUNÇÃO PARA RETORNAR AS UMIDADES RELATIVAS
def relUmid(nc):
    REL_UM = wrf.getvar(nc, "RH", timeidx=wrf.ALL_TIMES, method="cat")
    RELS = []

    for i in range(25):
        RELS.append(REL_UM[i][0][0][0])

    return RELS


# FUNÇÃO PARA RETORNAR A PRECIPITAÇÃO
def precip(nc):
    precs = wrf.getvar(nc, "PR", timeidx=wrf.ALL_TIMES, method="cat")
    precss = []

    for i in range(25):
        precss.append(precs[i][0][0][0])

    return precss