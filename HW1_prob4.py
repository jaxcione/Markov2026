import numpy as np 
import math
import statistics
import random
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def f_t(t): # pdf 
    if t<0:
        return 0
    if t>1:
        return 1
    else: 
        return 3*t**2
    
N=10**5 # n number of trials 
T_vals=[]
for k in range(N): # running 10**4
    Moe=np.random.uniform(0,1)#friend 1- randomly distrubted from 0 to 1
    Agnes=np.random.uniform(0,1)#friend 2-randomly distrubted from 0 to 1
    Dorothy=np.random.uniform(0,1)#friend 3-randomly distrubted from 0 to 1
    T=max(Moe,Agnes,Dorothy) # we get the max, s.t we know when the last friend arrives
    T_vals.append(T)

x_vals=np.linspace(0,1,1000)# x values go from 0 to 1 hour
y_vals=[]
for k in range(len(x_vals)):
   y_vals.append(f_t(x_vals[k]))#appending f(t) values into an array
    
plt.hist(T_vals,bins=40,density=True,color='skyblue',label="histogram") # creating histogram of 
plt.plot(x_vals,y_vals,color="red",label="PDF")
plt.xlim(0,1)
plt.xlabel("N")
plt.ylabel("Frequency")
plt.title("Histogram from 6Pm-7PM")
plt.legend()
plt.show()
