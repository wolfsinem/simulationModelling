import numpy as np 
import matplotlib.pyplot

def ho_euler():
    h = 0.1
    num_steps = 100

    e = np.zeros(num_steps+1)
    f = np.zeros(num_steps+1)

    e[0] = 1 
    for step in range(num_steps):
        e[step+1] = e[step] + e[step] * h
    return e

def ho_heun():
    h = 0.1
    num_steps = 100

    e = np.zeros(num_steps+1)
    f = np.zeros(num_steps+1)

    e[0] =1
    for step in range(num_steps):
        e[step+1] = e[step] + e[step] * h #euler
        e[step+1] = e[step] + ((e[step] + e[step + 1])/2) * h #heun
    return e
    




n = [5,10,20,100] # for x in n voor num_steps
