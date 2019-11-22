import numpy as np
import matplotlib.pyplot as plt

stnr = 1748884
def sir_model(stnr):
    populatie = int(str(stnr)[-2:])
    contacten = int(str(stnr)[3:-2]) 
    kans_infectie = float(str(stnr)[2])/100
    return populatie,contacten,kans_infectie

populatie, contacten,kans_infectie = sir_model(stnr)
print("De grootte van de populatie wordt {} miljoen, het gemiddelde aantal contacten per dag {} en de kans op infectie {}".format(populatie,contacten,kans_infectie))

h = 0.5 #days
trans_coeff = (kans_infectie * contacten) / populatie #day person
infectie_tijd = 5 #days 

end_time = 60 #days
num_steps = int(end_time / h)
times = h * np.array(range(num_steps + 1))

def seir_model(latency_time):  
    s = np.zeros(num_steps + 1)
    e = np.zeros(num_steps + 1)
    i = np.zeros(num_steps + 1)
    r = np.zeros(num_steps + 1)
    
    s[0] = populatie - 1e6 - 1e5 
    e[0] = 0
    i[0] = 1e5
    r[0] = 1e6
    
    for step in range(num_steps): 
        s2e = h * trans_coeff * s[step] * i[step]
        e2i = h / latency_time * e[step]
        i2r = h / infectie_tijd * i[step]
        
        s[step+1] = s[step] - s2e
        e[step+1] = e[step] + s2e - e2i 
        i[step+1] = i[step] + e2i - i2r
        r[step+1] = r[step] + i2r
        
    return s,e,i,r 

def plot_me():
    plt.subplot(211)
    plt.plot(times, e, label='S')
    plt.plot(times, e, label='E')
    plt.plot(times, i, label='I')
    plt.plot(times, r, label='R')
    plt.legend(loc="upper left")

    plt.subplot(212)
    plt.plot(times, s_2, label='S')
    plt.plot(times, e_2, label='E')
    plt.plot(times, i_2, label='I')
    plt.plot(times, r_2, label='R')
    plt.legend(loc="upper left")

    plt.show()

s,e,i,r = seir_model(1)
s_2,e_2,i_2,r_2 = seir_model(2)
plot_me()