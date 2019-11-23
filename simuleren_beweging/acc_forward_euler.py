import numpy as np 
import matplotlib.pyplot

def forward_euler():
    h=0.01 #s
    g=9.81 #m/s2
    stretch = 10
    m = 1000

    # force = m * g 
    # acceleration = F / m 

    num_steps = 1000
    t = np.zeros(num_steps+1) # tijd x-as
    x = np.zeros(num_steps+1) # hoogte y-as
    v = np.zeros(num_steps+1) # velocity / snelheid y-as

    x[0] = 10
    for step in range(num_steps):
        F = -stretch * v[step] + - g * x[step]
        acc = F/m
        t[step+1] = t[step] + h 
        x[step+1] = x[step] + h * v[step]
        v[step+1] = v[step] + acc
    return t,x,v
 
t,x,v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()

plot_me()