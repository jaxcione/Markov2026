import numpy as np
import random
import time
import matplotlib.pyplot as plt
import sympy 
import scipy 
from scipy.optimize import brentq

start=time.time()

def cdf(t):
    return (-t*np.exp(-t)-np.exp(-t)+1)

random_var=[]
for i in range(10**6):#making 10**6 random variables and 
    u=np.random.uniform()
    result=brentq(lambda p:cdf(p)-u,0,20) #0 being lower bound 20 being upper bound
    random_var.append(result)


end=time.time()
print(end-start)




