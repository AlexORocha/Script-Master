def windsvel(U, V):
    vel_vento = []
    for j in range(25):
        wind = (U[j]**2 + V[j]**2)**0.5
        vel_vento.append(wind)

    return vel_vento