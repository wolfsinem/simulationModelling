from main import pseudo_number_generator, plot_dist

"""
Pi benaderen met de 'Random Number Generator'
'Monte Carlo integration'
"""
def pi_benaderen():
    random_nums = pseudo_number_generator(num_steps=1000000,m=1)
    x = random_nums[:len(random_nums)//2]
    y = random_nums[len(random_nums)//2:]

    inside = 0
    outside = 0
    for (i,j) in zip(x,y):
        if math.sqrt(i**2+j**2) <=1:
            inside+=1
        else:
            outside+=1

    pi = (4.*inside)/len(zip(x,y))
    return pi