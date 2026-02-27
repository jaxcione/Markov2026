import numpy as np
import scipy as sp
import math 

q=.4
p=.35
s=.25
r_2=(1-math.sqrt(1-(4*p*q)))/(2*p)
i=10
N=100000

b=(-(p-q)/s)*((r_2)**i)+(i+(p-q)/s) #calculated value

for _ in range(10,N):
    u=np.random.random() #uniform random var
    state=10#current state
    if u<=q:
        state-=1 #decrease if we are less than q

    if u<=q+p:
        state+=1 #increase 1
    else:
        break #if we arent either we retire

print(state,"Simulated Value")
print(b,"Calculated Value")

