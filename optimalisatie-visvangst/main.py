import numpy as np 
import matplotlib.pyplot as plt 

maximum_growth_rate = 0.5
carrying_capacity = 2e6 

end_time = 10.
h = 0.1

num_steps = int(end_time / h)
times = h * np.array(range(num_steps + 1))

def logistic_growth():
    data_fish = []
    harvest_rates = [2e4, 5e4, 1e5, 2e5]
    fish = np.zeros(num_steps + 1)
    fish[0] = 2e5
    for harvest_rate in harvest_rates:
        is_extinct = False
        for step in range(num_steps):
            if is_extinct: 
                fish[step+1] = 0.
            else: 
                fish[step+1] = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
                if fish[step+1] <= 0.:
                    is_extinct = True
                    fish[step+1] = 0.
        data_fish.append(plt.plot(times,fish))
        plt.xlabel("Tijd in jaren")
        plt.ylabel("Aantal vissen")
        
    return fish

def harvest():
    data_result = []
    maximum_harvest_rate = 0.7 * 2.5e5
    ramp_start = 2.
    ramp_end = 6. 
    fish = np.zeros(num_steps + 1)
    fish[0] = 2e5
    """
    
    """
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
        # data_result.append()

    return fish

fish = logistic_growth()
fish = harvest()

def plot_me():
    plt.plot(times,fish)
    axes = plt.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')
    plt.show()
plot_me()