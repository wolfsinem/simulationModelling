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

# for num_steps in [5,10,20,100]:
#     x,y = euler_method(num_steps)

x,y = euler_method(5)
x2,y2 = euler_method(10)
x3,y3 = euler_method(20)
x4,y4 = euler_method(100)

def heun_method(num_steps):
    e = math.e
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

a, b = heun_method(20)

def plot_me():
    plt.plot(a,b,'r')
    # plt.plot(x2,y2, 'b')
    # plt.plot(x3,y3, 'g')
    # plt.plot(x4,y4, 'y')
    plt.show()
plot_me()