import sys
sys.path.append('/Users/wolfsinem/simulationModelling/genereren-pseudo-random-getallen')
from main import pseudo_number_generator

import math
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
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
f(x,a=1,mu=0,std=1) = a exp[-((x-mu)^2) / (2 * std)^2] = 
       
((1/wortel(2*pi))* exp(-(x^2) / 2))
"""

def gauss_distribution(sequence):
    """ Return gaussian distribution, m = mean, s = std"""
    m = mean(sequence)
    s = stdev(sequence)

    lijst = [] 

    for x in sequence:
        f  = 1/(s * (math.sqrt(2*math.pi)))
        f_ = f * np.exp(-.5*(((x-m)/s)**2))
        lijst.append(f_)
    
    return lijst

sequence = pseudo_number_generator(num_steps=1000)
lijst = gauss_distribution(sequence)

x = np.linspace(min(sequence),max(sequence),1000)
y = gauss_distribution(sequence)

# plt.plot(x,y)
# plt.show()
plt.hist(lijst)
plt.show()