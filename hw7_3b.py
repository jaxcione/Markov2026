import numpy as np
import scipy as sp
from scipy.integrate import quad
import math
from scipy.special import factorial
from scipy.stats import poisson

val=0

def lamda_t(t):
    return 0.5 * (1 + ( t/30 )**2)

def int_lamda(t):
    return 0.5 *((t**3/2700)+t)

t=np.linspace(0,120,10000)
y=quad(int_lamda,0,120)

for k in range(0,1000):
    val+=k*poisson.pmf(k, int_lamda(120))


print(val)