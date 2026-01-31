import numpy as np
import random
import statistics
import matplotlib.pyplot as plt

gamma=4
x0=10

def actual(t): #our PDF
    if t>=x0:
        return ((gamma-1)*(x0)**(gamma-1))*(t**(-gamma))
    else: 
        return 0

def inverse_function(u):#defining our inverse function
    return x0/((1-u)**(1/(gamma-1)))

x_vals=np.linspace(0,60,1000)
y_vals=[]
for k in range(len(x_vals)): #obtaining all the y values of the actual PDF
    y_vals.append(actual(x_vals[k]))

N=[100,1000, 10000] # number of samples in an array so I can easily loop through them


for i in N:#going through each number
    X_r=[]
    for j in range(i): #implementing the amount in each
        x=np.random.uniform(0,1) #random x  from 0-1
        X_r.append(inverse_function(x))#our random sample

    plt.hist(X_r,bins="fd",density=True,color="red",label=f"Histogram of samples:{i}") #density= true makes it normalized, binds="fd" uses Freedman–Diaconis rule to determine bin width
    plt.plot(x_vals,y_vals,color="blue",label="PDF")
    plt.xlim(0,60)
    plt.ylim(0,.35)
    plt.title("Histogram of X")
    plt.legend()
    plt.show()
    
    

