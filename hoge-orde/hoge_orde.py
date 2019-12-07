import math
import numpy as np
import matplotlib.pyplot as plt

e = math.e
h = 0.01

def euler_method(num_steps):
    x = np.zeros(num_steps+1)
    y = np.zeros(num_steps+1)

    x[0] = 0
    y[0] = 1

    for step in range(num_steps):
        x[step+1] = h * (step + 1)
        y[step+1] = y[step] + h * x[step]
    return x,y


# def heun_method(num_steps,h):
#     x = np.zeros(num_steps+1)
#     y = np.zeros(num_steps+1)

#     x[0] = 0
#     y[0] = 1

#     for step in range(num_steps+1):

n = [5,10,20,100]
for size in n:
    x,y = euler_method(size)

def plot_me():
    plt.plot(x,y)
    plt.show()

plot_me()