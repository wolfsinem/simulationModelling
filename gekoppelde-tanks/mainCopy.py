import matplotlib.pyplot as plt

def zout_oplossing(xas):
    TA = 100
    IA = 6
    TZA = 0
    ZI = 0.2
    UA = 4

    TB = 100
    IB = 3
    TZB = 20
    UB = 2 

    AB = 3
    BA = 1 
    
    times = [0]
    waarden_A = [0]
    waarden_B = [0]

    for x in range(xas):
        TA += (IA - UA)
        TZA += (ZI * IA)
        ZCA = (TZA/TA)

        TZA -= (ZCA*UA)

        TB += IB - (UB + BA)
        TZB += (ZCA*IB)
        ZCB = (TZB/TB)

        TZB -= (ZCB*UB) + (ZCA*BA)

        times.append(x)
        waarden_A.append(ZCA)
        waarden_B.append(ZCB)

    return times,waarden_A,waarden_B

time,tank_A, tank_B = zout_oplossing(200)

plt.plot(time, tank_A, 'r',label='tank_A')
plt.plot(time, tank_B, 'g',label='tank_B')
plt.title('Gekoppelde tanks met zoutoplossing')
plt.legend()
plt.show()
#test for github