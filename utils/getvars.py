from scipy.io import netcdf
from utils.params import DICT, ARQ_NAME
import wrf
import numpy as np

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
    U = []

    v = wrf.getvar(nc,"V", timeidx=wrf.ALL_TIMES, method="cat")
    V = []

    for i in range(25):
        U_i = u[i][0][0][0]
        U.append(U_i)
        
        V_i = v[i][0][0][0]
        V.append(V_i)        


    return U, V


# FUNÇÃO PARA RETORNAR A LATITUDE
def getlatlong(nc):
    Lat = wrf.getvar(nc,"XLAT", timeidx=wrf.ALL_TIMES, method="cat")[0][0][0]
    Long = wrf.getvar(nc,"XLONG", timeidx=wrf.ALL_TIMES, method="cat")[0][0][0]

    return Lat, Long


# FUNÇÃO PARA RETORNAR AS TEMPERATURAS
def temperature(nc):
    Temp = wrf.getvar(nc, "TSLB", timeidx=wrf.ALL_TIMES, method="cat")
    Temps = []

    for i in range(25):
        Temps.append(Temp[i][0][0][0] - 273)

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
    QVAPOR = wrf.getvar(nc, "QVAPOR", timeidx=wrf.ALL_TIMES, method="cat")
    TEMPS = temperature(nc)
    PRESSURE = pressure(nc)
    RELS = []

    svp1=611.2
    svp2=17.67
    svp3=29.65
    svpt0=273.15
    eps = 0.622

    for i in range(25):        
        #RH = (QVAPOR[i][0][0][0] * 100) / ( (pq0/PRESSURE[i]) * np.exp(a2*(TEMPS[i]-a3)/(TEMPS[i]-a4)) ) 
        q = QVAPOR[i][0][0][0]
        p = PRESSURE[i] * 100
        T = TEMPS[i] + 273

        RH = 100 * (p*q/(q*(1.-eps) + eps))/(svp1*np.exp(svp2*(T-svpt0)/(T-svp3)))
        #print(f'q: {q}, p: {p}, T: {T}')
        RELS.append(RH)

    return RELS

# FUNÇÃO PARA RETORNAR AS UMIDADES ESPECÍFICAS
def espUmid(nc):    
    ESP_UM = wrf.getvar(nc, "QVAPOR", timeidx=wrf.ALL_TIMES, method="cat")
    ESPS = []

    for i in range(25):
        ESPS.append(ESP_UM[i][0][0][0]*10**3)

    return ESPS


# FUNÇÃO PARA RETORNAR A PRECIPITAÇÃO
def precip(nc):
    precc = wrf.getvar(nc, "RAINC", timeidx=wrf.ALL_TIMES, method="cat")
    precnc = wrf.getvar(nc, "RAINNC", timeidx=wrf.ALL_TIMES, method="cat")
    precss = []

    for i in range(25):
        precss.append(precc[i][0][0] + precnc[i][0][0])

    return precss