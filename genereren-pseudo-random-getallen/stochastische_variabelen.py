from main import pseudo_number_generator
import matplotlib.pyplot as plt
import numpy as np 
import math
from statistics import mean, stdev


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
norm = pseudo_number_generator(num_steps=1000)

def gauss_distribution(sequence):
    """ Return gaussian distribution, m = mean, s = std"""
    m = mean(sequence)
    s = stdev(sequence)

    f = (2.*math.pi*s**2.) **-.5
    f_ = np.exp(-.5 * (x-m)**2. / s**2.) * f
    return f_

x = np.linspace(min(norm),max(norm),1000)
y = gauss_distribution(norm)
plt.plot(x,y)
plt.show()