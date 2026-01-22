import numpy as np 
import math
import statistics
import random
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# function u 

def f_u(u):
    return (u**4/((u**6+1)))

x_vals_log=np.arange(1,5.1,.1) # values from 1-5 in increments of .1
N_vals = np.floor(10**x_vals_log).astype(int) # getting the floor and making it an integer
En=[]
points=[]

for i in N_vals:
    count=0
    for j in range(i):  
        x_r = random.random() #random points fro 0,1
        y_r = random.random() #random points from 0,1
        points.append((x_r,y_r))
        if y_r <= f_u(x_r): # checking to see if the y value is less than the y value outputted by the function, then we append En
            count+= 1 # adding 1 
            
    En.append(count/i) #appending avg after all points from N_vals is added

En=np.array(En)


# plottinf curve and points
x_vals = np.linspace(0, 1, 100)
analytical=integrate.quad(f_u,0,1)
analytical_y=[]

for k in range(len(N_vals)):
    analytical_y.append(analytical[0]) # putting the analytical solution to the integral N times s.t I can plot it 
    
print(analytical)
y_vals = f_u(x_vals)
n_vals=np.linspace(0,1000,10000)

plt.figure(2)
plt.plot(x_vals, y_vals, label='f(u) curve',zorder=5)
plt.scatter(*zip(*points), color='lightgray', s=0.5, alpha=0.2, zorder=1, label='Points')
plt.plot
plt.ylim(0, 1)
plt.title("f(u) with Monte Carlo points")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.figure(1)
plt.plot(N_vals,En,color='red')
plt.plot(N_vals,analytical_y,color="blue")
plt.title("E(n) vs n")
plt.xscale("log")
plt.xlabel('ln(n)')
plt.ylabel("E(n)")






plt.show()
