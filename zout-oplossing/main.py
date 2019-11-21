import matplotlib.pyplot as plt
   
def zout_oplossing(xas,uitstroom):
    watertank = 1000
    instroom = 6
    totaal_zout = 0
    zout_in = 0.1

    times = [0]
    waarden = [0]

    for x in range(xas):
        watertank += instroom
        totaal_zout += (zout_in * instroom)
        zout_concentratie = (totaal_zout / watertank)

        watertank -= uitstroom
        totaal_zout -= (zout_concentratie * uitstroom)
        zout_concentratie = (totaal_zout / watertank)

        times.append(x)
        waarden.append(zout_concentratie)

    return times,waarden

times1, waarden1 = zout_oplossing(1000,6)
times2, waarden2 = zout_oplossing(1000,5)

plt.plot(times1, waarden1,'r',label='speed=6')
plt.plot(times2, waarden2,'g',label='speed=5')
plt.title('Zoutoplossing in een tank')
plt.legend()
plt.show()