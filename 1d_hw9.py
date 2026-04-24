import numpy as np
import scipy as sp
from scipy.integrate import quad
import math
import matplotlib.pyplot as plt

#params
alpha=1 
beta=1
L=60
N=10000

def r_k(k):#theoreticla
    return L*(L+1)/(2*alpha)-(1/(2*alpha)*k)-(1/(2*alpha)*k**2)

def simulate_cont(L,N):
    total_time=[]#storing total time
    for _ in range(N): #simulating N 
        #sttaring at state 0 and time 0
        current_state=0 
        current_time=0

        while current_state<L: #ensuring its less than L
            b_rate = beta if current_state > 0 else 0  # there exists no beta at state 0
            fowared_rate= alpha 
            tot=fowared_rate+b_rate
            #if at 0 the rate is 1 otherwise 1/2
            dt=np.random.exponential(1/tot)
            current_time+=dt #updaye time 
            u=np.random.random() #generating a random var 

            if u<(fowared_rate/tot): #if its less than 1/2 then add one
                current_state+=1 #add state
            else:
                current_state-=1 #else it goes back
        total_time.append(current_time)

    full_times=np.array(total_time)
    return full_times

simulate=simulate_cont(L,1000)
print("mean",np.mean(simulate))
print("var",np.var(simulate))

print('thoretical mean', r_k(0))