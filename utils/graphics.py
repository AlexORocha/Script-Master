import matplotlib.pyplot as plt

def plot(TIME, LAT, LONG, TEMP, PRESS, POT_TEMP, REL_HUM, U, V):  
    # PLOT DA FIGURA GLOBAL ------------------------------
    fig, ax1 = plt.subplots(figsize=(8,10))
    plt.title('\nPrevisão do BRAMS para\nLatitude %.5f, Longitude %.5f e Altura 760 m' %(LAT, LONG))
    ax1.set_xlabel('Tempo')
    # ----------------------------------------------------

    

    # FIGURA DE TEMPERATURA E PRESSÃO --------------------
    color = 'tab:red'  
    ax1.set_ylabel('Temperatura (ºC)', color=color)
    ax1.plot(TIME, TEMP, '-o', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Pressão (hPa)', color=color)
    ax2.plot(TIME, PRESS, '-o', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    # ----------------------------------------------------


    fig.tight_layout()

    #plt.savefig('Figure.png')
    plt.show()