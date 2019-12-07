import matplotlib.pyplot as plt
import numpy as np
   
def zout_oplossing(num_steps,uitstroom):
    # watertank = 1000
    instroom = 6
    zout_in = 0.1

    tank_1 = np.zeros(num_steps + 1)
    zout_1 = np.zeros(num_steps + 1) 
    conc_1 = np.zeros(num_steps + 1) 

    tank_1[0] = 1000
    zout_1[0] = 0
    conc_1[0] = zout_1[0] / tank_1[0]

    times = [0]
    waarden = [0]

    for step in range(num_steps):
        tank_1[step+1] = tank_1[step] + instroom - uitstroom
        zout_1[step+1] = zout_1[step] + (instroom * zout_in)
        conc_1[step+1] = zout_1[step] / tank_1[step]

        zout_1[step+1] = zout_1[step] - (conc_1[step] * uitstroom)
        conc_1[step+1] = zout_1[step] / tank_1[step]

        times.append(step)
        waarden.append(conc_1)

    return times,waarden

time_1, conc_1 = zout_oplossing(1000,5)
time_2, conc_2 = zout_oplossing(1000,6)

plt.plot(time_1,conc_1,'r',label='speed=5')
plt.plot(time_2,conc_2,'r',label='speed=6')
plt.title('Zoutoplossing in een tank')
plt.legend()
plt.show()