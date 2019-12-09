import numpy as np 
import math

#Linear Congenital Generator (LCG)
def pseudo_number_generator():
    x0 = 1
    a = 2
    c = 3
    m = 5 

    xn = x0
    new = ( a * Xn ) + c % m