import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

stnr = 1748884
def sir_model(stnr):
    populatie = int(str(stnr)[-2:]) * 1000000
    contacten = int(str(stnr)[3:-2]) 
    kans_infectie = float(str(stnr)[2])/100
    return populatie,contacten,kans_infectie

populatie, contacten,kans_infectie = sir_model(stnr)
print("De grootte van de populatie wordt {}, het gemiddelde aantal contacten per dag {} en de kans op infectie {}".format(populatie,contacten,kans_infectie))

h = 0.5 #days
trans_coeff = (kans_infectie * contacten) / populatie #day person
infectie_tijd = 5. #days 

end_time = 60 #days
num_steps = int(end_time / h)
times = h * np.array(range(num_steps + 1))

vaccinatie = int(populatie - ((1/infectie_tijd) / trans_coeff))
percentage_vaccinatie = int(100. / populatie * vaccinatie)
print("Er moeten {} mensen gevaccineerd worden om een epidemie te voorkomen, dit is {}% van de gehele populatie.".format(vaccinatie,percentage_vaccinatie))

def seir_model(latency_time):  
    s = np.zeros(num_steps + 1)
    e = np.zeros(num_steps + 1)
    i = np.zeros(num_steps + 1)
    r = np.zeros(num_steps + 1)
    
    s[0] = 1e8 - 1e6 - 1e5 
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
    ax1 = plt.subplot(211)
    ax1.set_title('Latency time of 1 day')
    plt.plot(times, e, label='S')
    plt.plot(times, e, label='E')
    plt.plot(times, i, label='I')
    plt.plot(times, r, label='R')
    plt.legend(loc="upper left")
    ax1.set(xlabel="Time in days",ylabel="Infected people")
    
    ax2 = plt.subplot(212)
    ax2.set_title('Latency time of 2 days')
    plt.plot(times, s_2, label='S')
    plt.plot(times, e_2, label='E')
    plt.plot(times, i_2, label='I')
    plt.plot(times, r_2, label='R')
    plt.legend(loc="upper left")
    ax2.set(xlabel="Time in days",ylabel="Infected people")

    plt.tight_layout()
    plt.show()

s,e,i,r = seir_model(1)
s_2,e_2,i_2,r_2 = seir_model(2)
plot_me()
