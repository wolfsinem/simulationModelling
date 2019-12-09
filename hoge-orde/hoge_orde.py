import math
import numpy as np
import matplotlib.pyplot as plt

def euler_method(num_steps):
    h = 0.01
    x = np.zeros(num_steps+1)
    y = np.zeros(num_steps+1)

    x[0] = 0
    y[0] = 1

    for step in range(num_steps):
        x[step+1] = x[step] + h 
        y[step+1] = y[step] + h * x[step]
    return x, y

def heun_method(num_steps):
    h = 0.01
    x = np.zeros(num_steps+1)
    y = np.zeros(num_steps+1)

    x[0] = 0
    y[0] = 1

    for step in range(num_steps):
        xE = x[step] + h * y[step]
        yE = y[step] + h

        x[step+1] = x[step] + h * 0.5 * (y[step] + yE)
        y[step+1] = y[step] + h * 0.5
    return x, y 

def plot_me(benadering):
    for n in [5,10,20,100]:
        x,y = benadering(n)
        plt.plot(x,y,'r')
        plt.show()
plot_me(euler_method)
plot_me(heun_method)