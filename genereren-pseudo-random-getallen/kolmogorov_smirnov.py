import numpy as np 
from main import pseudo_number_generator

"""
http://people.cs.pitt.edu/~lipschultz/cs1538/05_random_numbers.pdf

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
    data = pseudo_number_generator(num_steps=5,a=100,c=101427,m=2**16)
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
    
    maxP = 0.0 
    for n in d_plus:
        if n > maxP:
            maxP = n

    maxM = 0.0
    for n in d_min:
        if n > maxM:
            maxM = n
    print('Max voor D+ = {} & max voor D- = {}'.format(maxP,maxM))

    if maxP > maxM:
        maxD = maxP
    else:
        maxD = maxM
    print('Maximum deviatie is dus: {}'.format(maxD))

    alphaValue = 0.05    
    if maxD > alphaValue:
        print('Maximum deviatie: {}, is groter dan alpha {}'.format(maxD,alphaValue))
        print('We verwerpen H0 en conluderen dat de distributie niet uniform is')
    else:
        print('Maximum deviatie: {}, is kleiner dan alpha: {}'.format(maxD,alphaValue))
        print('We verwerpen H0 niet en daarmee concluderen we dat de distributie uniform is')

    return maxP,maxM,maxD,alphaValue

maxP,maxM,maxD,alphaValue = kolmogorov_smirnov()