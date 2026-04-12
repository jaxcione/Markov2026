import numpy as np
import scipy as sp
from scipy.integrate import quad


def lamda_t(t):
    return 0.5 * (1 + ( t/30 )**2)

def int_lamda(t):
    return 0.5 *((t**3/2700)+t)

def f(t):
    return t*lamda_t(t) * np.exp(-1*int_lamda(t))

t=np.linspace(0, 1000000, 1000)
y=f(t)
result=quad(f,0,np.inf)
print(result)

