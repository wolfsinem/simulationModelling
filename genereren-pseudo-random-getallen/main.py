import numpy as np 
import math
import statistics
import matplotlib.pyplot as plt

def pseudo_number_generator(num_steps=10,previous=None, a=214013,c=2531011,m=2**32):
    if previous is None:
        x = math.pi
    else:
        x = previous

    lijst = []
    for i in range(num_steps):
        n = (a*x+c)%m
        x = n
        lijst.append(n)
    # print('Er zijn {} random numbers gegenereerd met lineaire congruentie met parameters a = {}, c = {} en m = {}'.format(num_steps,a,c,m))
    return lijst

sequence = pseudo_number_generator()

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
def kolmogorov_smirnov(data,n):
    a = np.sort(data)
    max_d_plus = 0
    max_d_min = 0
    for i in range(n):
        dnplus = (i/n) - a[i]
        if dnplus > max_d_plus:
            max_d_plus = dnplus
        dnminus = a[i] - (i-1)/n
        if dnminus > max_d_min:
            max_d_min = dnminus
    dn = max(max_d_plus,max_d_min)
    return dn

k = kolmogorov_smirnov(sequence,10)
print(k)

# 3905047056.625

# def std():
#     result = []
#     steps = []
#     for i in range(0,101):
#         num = pseudo_number_generator(previous=i)
#         count = statistics.variance(num)
#         result.append(count)
#         steps.append(i)
#     return steps,result

# x,y = std()

def plot_me(xas,yas):
    plt.scatter(xas,yas)
    plt.xlabel('seed')
    plt.ylabel('variantie')
    plt.show()
# plot_me(x,y)