import math
import numpy as np
import matplotlib.pyplot as plt

e = math.e
def euler_method(num_steps,h):
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

x, y = euler_method(100,0.01)
plt.plot(x,y)
plt.show()
