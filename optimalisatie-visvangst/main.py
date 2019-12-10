#%%
import numpy as np 
import matplotlib.pyplot as plt 

"""
Exposential growth with harvesting
f(t)punt = (maximum_growth_rate / years) f(t) - 4 * 10^5(tons/year)

Logistic growth constant harvesting
f(t)punt = (maximum_growth_rate / year) (f(t)-10^6tons) - 10^5(tons/year)
-------------------------------------------------------------------------
harvest() function shows when no harvesting is taking place
At the beginning there is expontential growth but after a while
the amount of fish will approach the maximum carrying capacity
"""
def harvest():
    maximum_growth_rate = 0.5
    carrying_capacity = 2e6 
    end_time = 10.
    h = 0.1
    num_steps = int(end_time / h)
    times = h * np.array(range(num_steps + 1))
    data = []
    maximum_harvest_rate = 0.7 * 2.5e5
    ramp_start = 2.
    ramp_end = 6. 
    fish = np.zeros(num_steps + 1)
    fish[0] = 2e5

    is_extinct = False
    for step in range(num_steps):
        time = h * step
        harvest_factor = 0.0;
        if time > ramp_end:
            harvest_factor = 1.0
        elif time > ramp_start:
            harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)
        harvest_rate = harvest_factor * maximum_harvest_rate
        
        if is_extinct:
            fish[step+1] = 0.
        else:
            fish[step+1] = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
            if fish[step+1] <= 0.:
                is_extinct = True
                fish[step+1] = 0.
        fish[step+1] = fish[step+1]

    return fish

def total_harvest():
    maximum_growth_rate = 0.5
    carrying_capacity = 2e6 
    maximum_harvest_rate = 0.7 * 2.5e5 #vangst mag maar toenemen tot 0.7 MSY 

    end_time = 10. 
    h = 0.1 
    num_steps = int(end_time / h)
    times = h * np.array(range(num_steps + 1))

    fish = np.zeros(num_steps + 1) 
    fish[0] = 2e5

    results = []

    for ramp_start in np.arange(2., 10.01, 0.5): #ramp mag pas over 2 jaar starten 
        for ramp_end in np.arange(ramp_start, 10.01, 0.5): 
            total_harvest = 0.
            is_extinct = False
            for step in range(num_steps):
                time = h * step 
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)    
                harvest_rate = harvest_factor * maximum_harvest_rate
                if is_extinct:
                    current_harvest = 0.
                    fish[step+1] = 0.
                else:
                    current_harvest = h * harvest_rate
                    fish[step+1] = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
                    if fish[step+1] <= 0.:
                        is_extinct = True
                        current_harvest = fish[step]
                        fish[step+1] = 0.
                fish[step + 1] = fish[step+1]
                total_harvest += current_harvest
            results.append([ramp_start, ramp_end, total_harvest])

    return results

"""
The result shows that there is not a single combination of start and end time, 
but rather a line of combinations.
"""
fish = harvest()
results = total_harvest()

def plot_me():
    plt.plot(times,fish)
    axes = plt.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')
    plt.show()
plot_me()

def plot_total_harvest():
    plt.scatter([r[0] for r in results], [r[1] for r in results], [5e-11 * r[2] ** 2. for r in results], edgecolor = 'none')
    axes = plt.gca()
    axes.set_xlabel('Ramp start in years')
    axes.set_ylabel('Ramp end in years')
plot_total_harvest()

# %%
