import numpy as np 
import math

#Linear Congenital Generator (LCG)
def pseudo_number_generator(previous):
    if previous is None:
        x = 1
    else:
        x = previous

    a = 2
    c = 3
    m = 5 
    return (a*x+c)%m

def sequence():
    list = []
    for i in range(5):
        n = pseudo_number_generator(i)
        list.append(n)
    return list

a = sequence()
print(a)

"""
pseude_numer_generator(None)  output: 0 
pseude_numer_generator(0)     output: 3 
pseude_numer_generator(3)     output: 4
pseude_numer_generator(4)     output: 1 

x1 = 2 * 1 + 3 (mod 5)
   = 0
x2 = 2 * 0 + 3 (mod 5)
   = 3 
x3 = 2 * 3 + 3 (mod 5)
   = 4 
x4 = 2 * 4 + 3 (mod 5)
   = 1 
"""