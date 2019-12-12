import numpy as np 
import math
import statistics
import matplotlib.pyplot as plt

def pseudo_number_generator(num_steps=1000,previous=None, a=3209867,c=12493,m=2**80):
    if previous is None:
        x = math.pi
    else:
        x = previous
        
    list = []
    for i in range(num_steps):
        n = (a*x+c)%m
        x = n
        list.append(n)
    return list

def std():
    result = []
    num_steps = []
    for i in range(0,101):
        num = pseudo_number_generator(previous=i)
        count = statistics.variance(num)
        result.append(count)
        num_steps.append(i)
    return num_steps,result

x,y = std()

def plot_me(xas,yas):
    plt.plot(xas,yas)
    plt.xlabel('seed')
    plt.ylabel('variantie')
    plt.show()
plot_me(x,y)