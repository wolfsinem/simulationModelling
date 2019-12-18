import numpy as np 
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

def pseudo_number_generator(num_steps,previous=None, a=214013,c=2531011,m=2**32):
    if previous is None:
        x = 10**-10
    else:
        x = previous

    lijst = []
    for i in range(num_steps):
        n = (a*x+c)%m
        x = n
        lijst.append(n)
    return lijst

def plot_dist():
    fig, axes = plt.subplots(1,2)
    num_steps = [10,10**6]
    for i,t in enumerate(num_steps):
        sns.distplot(pseudo_number_generator(t),ax=axes[i])
        axes[i].set_title('n={}'.format(t))
    fig.suptitle('Distribution pseudo random numbers')
    plt.show()