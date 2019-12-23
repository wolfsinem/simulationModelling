from main import pseudo_number_generator
import matplotlib.pyplot as plt
import numpy as np 
import math

"""
Stochastische variabelen genereren uit een verdeling naar keuze.
https://people.engr.ncsu.edu/hp/files/simulation.pdf

Random numbers following a specific distribution are called
stochastic variates.

f(x) = a exp[-((x-mu)^2) / (2 * std)^2]
a = 1.0 
mu = 5.0
std = 2.0

Box-Muller Transform 
U1 = [0,1] random numbers between 0 en 1
U2 = [0,1] random numbers between 0 en 1

x = wortel(-2 * LnU1 * cos(2*pi*U2))
f(x,a=1,mu=0,std=1) = a exp[-((x-mu)^2) / (2 * std)^2] = ((1/wortel(2*pi))* exp(-(x^2) / 2))

normal --> gaussian
x = mu + (std * (wortel(-2 * LnU1 * cos(2*pi*U2))))

if (U1 == 0):
 x = 0
"""
norm_1 = pseudo_number_generator(num_steps=10,m=1)

def gauss(m,s):
    """ Return gaussian distribution, m = mean, s = std"""

    x = pseudo_number_generator(num_steps=10,m=1)
    h = np.exp(-(x-m)**2. / (2. * s**2.))

    return h / h.sum()


# mean, sigma = 1, 0.2 
# gaussian = np.random.normal(mean,sigma,size=1000)

# bins = 30
# plt.hist(gaussian, bins)
# plt.show()