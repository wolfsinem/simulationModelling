from main import pseudo_number_generator
import math
import numpy as np
import matplotlib.pyplot as plt

"""
Pi benaderen met de 'Random Number Generator'
'Monte Carlo integration'

https://measureofdoubt.com/2018/07/22/finding-pi-from-random-numbers/

"""
def pi_benaderen():
    pseudo_nums = pseudo_number_generator(num_steps=1000000,m=1)
    x = pseudo_nums[:len(pseudo_nums)//2]
    y = pseudo_nums[len(pseudo_nums)//2:]

    inside = [[],[]]
    outside = [[],[]]
    total_inside = 0
    total_outside = 0
    for (i,j) in zip(x,y):
        if math.sqrt(i**2+j**2)**0.5 <=1:
            inside[0].append(i)
            inside[1].append(j)
            total_inside+=1
        else:
            outside[0].append(i)
            outside[1].append(j)
            total_outside+=1

    pi = (4.*total_inside)/len(zip(x,y))
    print('Pi benadering bij random gegenereerde getallen: {}'.format(pi))
    return inside,outside

def plot_cirkel():
    x,y = pi_benaderen()
    theta = np.linspace(0, np.pi/2, 100)
    r = np.sqrt(1.0)

    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)
    ax.set_aspect(1)

    plt.scatter(x[0],x[1])
    plt.scatter(y[0],y[1])

    plt.grid(linestyle='--')
    plt.show()

plot_cirkel() 