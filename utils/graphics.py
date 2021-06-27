import matplotlib.pyplot as plt

def plot(TIME, LAT, LONG, TEMP, PRESS, POT_TEMP, REL_HUM, SPECIF_HUM, U, V, PREC):  
    # PLOT DA FIGURA GLOBAL ------------------------------
    fig, (ax1, ax3) = plt.subplots(2, figsize=(8,6), sharex=True)
    # ----------------------------------------------------

    # FIGURA DO VENTO ------------------------------------
    ax1.set_title('\nPrevisão do BRAMS para\nLatitude %.5f, Longitude %.5f e Altura 760 m' %(LAT, LONG))

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

    fig.tight_layout()

    #plt.savefig('Figure.png')
    

    plt.show()