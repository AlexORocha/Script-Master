import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
import matplotlib.cm as cm
import numpy as np
import cartopy.crs as ccrs
from utils.winds_function import windsvel


def plot(TIME, LAT, LONG, TEMP, PRESS, POT_TEMP, REL_HUM, SPECIF_HUM, U, V, PREC):  
    # PLOT DA FIGURA GLOBAL ------------------------------
    fig, (ax0, ax1, ax3, ax4) = plt.subplots(4, figsize=(8,10), sharex=True)
    # ----------------------------------------------------

    # FIGURA DO VENTO ------------------------------------
    vel_vento = windsvel(U, V)
    ax0.barbs(TIME, PRESS, U, V)

    color = '0'
    ax0.set_title('\nPrevisão do BRAMS para\nLatitude %.5f, Longitude %.5f e Altura 760 m' %(LAT, LONG))
    ax0.set_ylabel('Vento (m/s) - Theta (k)')
    #ax0.plot(TIME, PRESS, '-0', color=color)
    ax0.tick_params(axis='y', labelcolor=color)
    #ax0.barbs(U, V)
    ax0.grid()    
    # ----------------------------------------------------


    # FIGURA DE TEMPERATURA E PRESSÃO --------------------
    color = '0'
    ax1.set_ylabel('Pressão (hPa)', color=color)
    ax1.plot(TIME, PRESS, '-o', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    #ax1.set_xlabel('Tempo')

    ax2 = ax1.twinx()

    color = 'tab:red'  
    ax2.set_ylabel('Temperatura (ºC)', color=color)
    ax2.plot(TIME, TEMP, '-o', color=color)
    ax2.tick_params(axis='y', labelcolor=color) 
    ax1.grid()
    # ----------------------------------------------------

    # FIGURA DE UMIDADE RELATIVA (%) ---------------------    
    color = '0'
    ax3.set_ylabel('Umidade Relativa (%)', color=color)
    ax3.plot(TIME, REL_HUM, '-o', color=color)
    ax3.tick_params(axis='y', labelcolor=color)
    ax3.grid()
    # ----------------------------------------------------


    # FIGURA DA PRECIPITAÇÃO -----------------------------
    color = '0'
    ax4.set_ylabel('Precipitação (mm/hr)', color=color)
    ax4.plot(TIME, PREC, '-o', color=color)
    ax4.tick_params(axis='y', labelcolor=color)
    ax4.grid()
    ax4.set_ylim([0, 100])
    # ----------------------------------------------------

    # ADICIONANDO A FIGURA DO MASTER ---------------------
    #im = plt.imread(get_sample_data('/media/alex/alexNoteHD/Outros/Script Master/master_logo.jpeg'))
    #master = fig.add_axes([0.40, 0.07, 0.2, 0.2], anchor='NW')
    #master.imshow(im)
    #master.axis('off')

    fig.tight_layout()

    #plt.savefig('Figure.png')
    

    plt.show()