# import sys
# sys.path.append('/Users/wolfsinem/simulationModelling/genereren-pseudo-random-getallen')
# from main import pseudo_number_generator
import numpy as np # use numpy for scientific computations with matrices, arrays or large datasets
import matplotlib.pyplot as plt

"""
Stochastische variabelen genereren uit een verdeling naar keuze. 
https://people.engr.ncsu.edu/hp/files/simulation.pdf
https://glowingpython.blogspot.com/2013/01/box-muller-transformation.html 

Random numbers following a specific distribution are called
stochastic variates.

f(x) = a exp[-((x-mu)^2) / (2 * std)^2]
a = 1.0 
mu = 5.0
std = 2.0

Box-Muller Transform 
U1 = [0,1] random numbers between 0 en 1
U2 = [0,1] random numbers between 0 en 1

z1 = (wortel(-2 * lin(u1))) * cos (2*pi*u2) 
z2 = (wortel(-2 * lin(u1))) * sin (2*pi*u2)
"""
def pseudo_number_generator(num_steps,previous=10**-10,a=214013,c=2531011,m=2**32):
    x = previous
    lijst = []
    for i in range(num_steps):
        x = (a*x+c)%m
        lijst.append(x)
    return [i/m for i in lijst]

def gauss_distribution():
    """Transformation function using Gaussian Distribution"""
    # use the pseudo random number generator again to generate x values
    u1_ = pseudo_number_generator(num_steps=10000) 
    u2_ = pseudo_number_generator(num_steps=10000) 

    z1 = np.sqrt(-2 * np.log(u1) for u1 in u1_) * np.cos(2 * np.pi * (u2)for u2 in u2_)
    z2 = np.sqrt(-2 * np.log(u1) for u1 in u1_) * np.sin(2 * np.pi * (u2)for u2 in u2_)
    return z1,z2

# new generated values with the gauss distribution function
z1,z2 = gauss_distribution()