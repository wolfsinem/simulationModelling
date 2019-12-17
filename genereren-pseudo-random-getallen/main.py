import numpy as np 
import math
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

def printLine():
    print('-------------------------------------------------------------------------------------------------------------')

def pseudo_number_generator(num_steps,previous=None, a=214013,c=2531011,m=2**32):
    if previous is None:
        x = math.pi
    else:
        x = previous

    lijst = []
    for i in range(num_steps):
        n = (a*x+c)%m
        x = n
        lijst.append(n)
    printLine()
    # print('Er zijn {} random numbers gegenereerd met lineaire congruentie met parameters: a = {}, c = {} en m = {}'.format(num_steps,a,c,m))
    # print('De lijst met gegenereerde random numbers: {}'.format(lijst))
    printLine()
    return lijst

def plot_dist():
    fig, axes = plt.subplots(1,2)
    num_steps = [10,10**6]
    for i,t in enumerate(num_steps):
        sns.distplot(pseudo_number_generator(t),ax=axes[i])
        axes[i].set_title('n={}'.format(t))
    fig.suptitle('Distribution pseudo random numbers')
    plt.show()
# plot_dist()

"""
Suppose we generate N values with RNG. Consider the empirical distribution based on these N values.
Let Sn(x) be the % of N values that are <= x, for any value x.
For example: 
        - Sn(0.25)
        - Sn(0.5)
        - Sn(0.75)
The KS checks to see what the biggest deviation of Sn(x) from f(x) is. 
If max Sn(x) - f(x) is very large, we reject the null hypothesis
---------------------------------------------------------------------------------------------------
Procedure of the KS test:
1) sort data
2) compute D+ = max{i/N - R(i)}
3) compute D- = max{R(i) - (i-l)/N}
4) compute D  = max(D+,D-)
5) find Dstd in table for the desired lvl of std and sample size N
    if D > Dstd, recject null hypothesis
"""
def kolmogorov_smirnov():
    data = pseudo_number_generator(5)
    ri = np.sort(data)
    n = len(data)
    
    d_plus = []
    d_min = []
    maxD = 0.0

    for i in range(n):
        dPlus = (i/n) -  ri[i]
        if dPlus > 0: 
            d_plus.append(dPlus)
        
        dMinus = ri[i] - (i-1)/n
        if dMinus > 0: 
            d_min.append(dMinus)
    
    # print('Berekende D+:{}'.format(d_plus))
    # print('Berekende D-:{}'.format(d_min))
    printLine()

    maxP = 0.0 
    for n in d_plus:
        if n > maxP:
            maxP = n
    # print('Max voor D+:{}'.format(maxP))

    maxM = 0.0
    for n in d_min:
        if n > maxM:
            maxM = n
    # print('Max voor D-:{}'.format(maxM))

    if maxP > maxM:
        maxD = maxP
    else:
        maxD = maxM

    # print('Maximum deviatie: {}'.format(maxD))
    printLine()
    return d_plus,d_min,maxP,maxM,maxD
    
dP,dM,maxP,maxM,maxD = kolmogorov_smirnov()

"""
Pi benaderen met de 'Random Number Generator'
"""
def plot_cirkle():
    theta = np.linspace(0, np.pi/2, 100)
    r = np.sqrt(1.0)

    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)
    ax.set_aspect(1)

    plt.grid(linestyle='--')
    plt.show()
    
plot_cirkle()