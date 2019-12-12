import numpy as np 
import math

#Linear Congenital Generator (LCG)
def pseudo_number_generator(num_steps=5,previous=None, a=2,c=3,m=5):
    if previous is None:
        x = 1
    else:
        x = previous
        
    list = []
    for i in range(num_steps):
        n = (a*x+c)%m
        x = n
        list.append(n)
    return list

a = pseudo_number_generator()
print(a)

"""
pseude_numer_generator(None)  output: 0 
pseude_numer_generator(0)     output: 3 
pseude_numer_generator(3)     output: 4
pseude_numer_generator(4)     output: 1 
pseude_numer_generator(1)     output: 0

x1 = 2 * 1 + 3 (mod 5)
   = 0
x2 = 2 * 0 + 3 (mod 5)
   = 3 
x3 = 2 * 3 + 3 (mod 5)
   = 4 
x4 = 2 * 4 + 3 (mod 5)
   = 1 
"""