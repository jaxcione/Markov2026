import numpy as np
import scipy as sp
from scipy.integrate import quad
import math
from scipy.special import factorial
from scipy.stats import poisson
import matplotlib.pyplot as plt

val=0
t_i_store=[] #storing vals here
new_vals=[]
s=0#treating this as time
def lamda_t(t):
    return 0.5 * (1 + ( t/30 )**2)

def int_lamda(t):
    return 0.5 *((t**3/2700)+t)

max_lam=max(lamda_t(t) for t in np.linspace(0,120,10000))#maximum lam(t)
print("Maximum value of lambda(t) over [0,120]:", max_lam)

while s<120:
    u=np.random.uniform(0,1) #gerneating a random variable
    dt=(np.log((1-u))/-max_lam) #the interarrival times or times inbetween
    s+=dt #our arrival time
    if s<120:
        t_i_store.append(s) #storing our arrival time
    

#removing lams 
for k in range(len(t_i_store)):
    
    if np.random.random()<(lamda_t(t_i_store[k]))/max_lam:
        new_vals.append(t_i_store[k])

text=len(new_vals)


days=np.linspace(0,120,10000)
plt.hist(new_vals,bins=120, density=False, alpha=0.6, color='g', label=f'Simulated Data' )
plt.plot([],[],'',label=f"Number of Arrivals{text}")
plt.xlabel('Days')
plt.ylabel('Times per Day')
plt.title(f'Histogram of Simulated Arrival Times')
plt.legend()
plt.show()