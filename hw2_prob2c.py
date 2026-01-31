import numpy as np
import random
import time
import matplotlib.pyplot as plt
import sympy 
import scipy 
from scipy.optimize import root

start=time.time()

def f_div_g(x):
    return ((np.e*x/2)*(np.exp(-x/2)))

counter=0
storage=[]

while len(storage)<10**6: #run a while because we dont know how many samples we are generating(because we are rejecting some)
    u=np.random.uniform()#gerneating random samples
    x_exp=np.random.exponential(scale=2) #getting exponential distributed values
    if u<=f_div_g(x_exp):
        storage.append(x_exp)
    else: 
        counter+=1
        continue

end=time.time()
print("Acceptance Rate: ", len(storage)/(len(storage)+counter))
print(f"Time to run: {end-start}")


