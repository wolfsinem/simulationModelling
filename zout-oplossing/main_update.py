import matplotlib.pyplot as plt
import numpy as np
   
def zout_oplossing(num_steps,uitstroom):
    instroom = 6
    zout_in = 0.1 

    t = np.zeros(1000 + 1) 
    z = np.zeros(1000 + 1) 
    c = np.zeros(1000 + 1)  

    t[0] = 1000
    z[0] = 0
    c[0] = z[0] / t[0]

    times = [1]
    for step in range(num_steps):
        t[step+1] = t[step] + instroom - uitstroom
        z[step+1] = z[step] + (instroom * zout_in) - (uitstroom * c[step])
        c[step+1] = z[step] / t[step]
        
        times.append(step)
    
    return times, c

times, conc_tank_1 = zout_oplossing(1000,6)
times, conc_tank_2 = zout_oplossing(1000,5)

plt.plot(times,conc_tank_1,'r',label='uitstroom=6')
plt.plot(times,conc_tank_2,'r',label='uitstroom=5')
plt.title('Zoutoplossing in een tank')
plt.legend()
plt.show()