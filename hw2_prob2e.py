import numpy as np
import random
import time
import matplotlib.pyplot as plt
import sympy 
import scipy
from scipy.stats import gamma

# storage=[]
# while len(storage)<10**6:
#     u=np.random.exponential(1)
#     z=np.random.exponential(1)
#     storage.append(u+z)

# x_vals=np.linspace(0,10,1000)
# y_vals=gamma.pdf(x_vals,a=2,scale=1)


# plt.hist(storage,bins=100,density=True,color="purple",label="Histogram of the Sum of Two Exponentials")
# plt.plot(x_vals,y_vals,color="red",label="Gamma Function")
# plt.legend()
# plt.show()



def f_div_g(x):
    return ((np.e*x/2)*(np.exp(-x/2)))

def pdf(t):
    return (t*np.exp(-t))

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

x_vals=np.linspace(0,10,100)
y_vals=pdf(x_vals)

plt.hist(storage,bins=100,density=True,color="purple",label="Accept vs Reject Method")
plt.plot(x_vals,y_vals,label="PDF")
plt.legend()
plt.show()
