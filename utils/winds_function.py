def windsvel(U, V):
    vel_vento = []
    for i in range(25):
        wind = (U[i]**2 + V[i]**2)**0.5
        vel_vento.append(wind)

    return vel_vento