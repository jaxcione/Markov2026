import numpy as np
import matplotlib.pyplot as plt
import random

c=(7+4*np.sqrt(3))/(6*np.exp(np.sqrt(3)-1))
a=-1+np.sqrt(3)

def f(x):
    return  1/3*(x)*(1+x)*np.exp(-x)

def g(x):
    return ((a**2)*x*np.exp(-a*x))

x_vals=np.linspace(0,35,1000)

g_y=g(x_vals)
f_y=f(x_vals)

plt.plot(x_vals,f_y,label="f(x)")
plt.plot(x_vals,c*g_y,label="g(x)")
plt.xlabel("x ")
plt.ylabel("y")
plt.legend()
plt.show()