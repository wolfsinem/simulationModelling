import sys
sys.path.append('/Users/wolfsinem/simulationModelling/genereren-pseudo-random-getallen')
from main import pseudo_number_generator
from numpy import sqrt, log, sin, cos, pi as np # use numpy for scientific computations with matrices, arrays or large datasets
import seaborn as sns
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

def gauss_distribution():
    """Transformation function using Gaussian Distribution"""
    # use the pseudo random number generator again to generate x values
    u1_ = pseudo_number_generator(num_steps=10000) 
    u2_ = pseudo_number_generator(num_steps=10000) 

    z1 = math.sqrt(-2 * math.log(u1) for u1 in u1_) * math.cos(2 * math.pi * (u2)for u2 in u2_)
    z2 = math.sqrt(-2 * math.log(u1) for u1 in u1_) * math.sin(2 * math.pi * (u2)for u2 in u2_)
    return z1,z2

# new generated values with the gauss distribution function
z1,z2 = gauss_distribution()

# plot data and see if its normally distributed
plt.subplot(221)
plt.hist(z1, bins=20)
plt.title('')

plt.subplot(222)
plt.hist(z2, bins=20)
plt.title('')
# plt.show()