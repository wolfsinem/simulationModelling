import numpy as np 
import matplotlib.pyplot

def forward_euler():
    h=0.01 # small time steps of size    s
    g=9.81 # valversnelling  constant    m/s2
    friction = 0.1 # wrijving 
    num_steps = 100

    t = np.zeros(num_steps+1) # tijd x-as
    x = np.zeros(num_steps+1) # hoogte y-as
    v = np.zeros(num_steps+1) # velocity / snelheid y-as

    # implementeer de Euler-integratie en simuleer een valbeweging
    for step in range(num_steps):
        t[step+1] = t[step] + h # tijd berekenen
        x[step+1] = x[step] + h * v[step] # hoogte berekenen
        v[step+1] = - g * h + v[step] # velocity 
        
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
