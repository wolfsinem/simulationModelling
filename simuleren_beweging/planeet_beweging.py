#%% 
import numpy as np
import matplotlib.pyplot as plt
import math

# Gebruik Euler integratie om een planeet- of komeetbeweging te simuleren
# Udacity

h = 0.1

def acceleration(position):
    earth_mass = 5.97e24
    gravitational_constant = 6.67e-11
    vector = - position 
    return gravitational_constant * earth_mass / np.linalg.norm(vector) ** 3 * vector

def ship():
    num_steps = 130000 #higher steps = more accurate 
    x = np.zeros([num_steps + 1,2]) 
    v = np.zeros([num_steps + 1,2])  

    x[0,0] = 15e6
    x[0,1] = 1e6
    v[0,0] = 2e3
    v[0,1] = 4e3

    # forward_euler method 
    for step in range(num_steps):
        x[step+1] = x[step] + h * v[step] #position (inside acceleration function)
        v[step+1] = v[step] + h * acceleration(x[step]) #velocity
    return x,v

x,v = ship()

def plot_me():
    plt.axis('equal')
    plt.plot(x[:,0],x[:,1]) #spaceship moving around the earth
    plt.scatter(0,0) #this is the earth
    axes = plt.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()

# elipse isnt closing at around (1.5;0.0) and that shows that euler uses approximations
# if u use more exact expressions for position/velocity you end up with a closed elipse

# %%
