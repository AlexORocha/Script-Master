# IMPORT DOS MÓDULOS ------------------------
from utils.getvars import *
from utils.params import *
from utils.graphics import *
#--------------------------------------------

def run():
    # LEITURA DO ARQUIVO .NC ----------------
    file = getvars()
    # ---------------------------------------

    # VERIFICA A LATITUDE E LONGITUDE DO PLOT
    lat, long = getlatlong(file)
    # ---------------------------------------

    # CAPTURA OS PARÂMETROS DE PLOT ---------
    time = measTime(file)
    temp = temperature(file)
    press = pressure(file)
    pot_temp = potTemp(file)
    u, v = winds(file)
    rel_hum = relUmid(file)
    specif_hum = espUmid(file)
    prec = precip(file)
    # ---------------------------------------

    # PLOT DA FIGURA ------------------------
    plot(time, lat, long, temp, press, pot_temp, rel_hum, specif_hum, u, v, prec)
    # ---------------------------------------

    