import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
import statistics

s,n=sp.symbols('s n', real=True, positive=True) # what symbols we are using
phi_Y = sp.exp((n*(sp.exp(s/sp.sqrt(n)) - 1) - s*sp.sqrt(n))) # phi_Y as a function

#Note: to go to infinity us sp.oo.--> sp.series(function, variable, point, n terms (keep in mind if n=10 it shows n-1 terms))
series_exp_1=sp.series(phi_Y,s,0,n=10) # expanding the series(phi) w repect to s, starting at 0. Taking the first 10 terms

derivitive_1=sp.diff(series_exp_1,s) # first derivitive w respect to s
second_deriv=sp.diff(derivitive_1,s) #second derivitve
sd=sp.diff(second_deriv,s) #third deriv

deriv_at_0_d1=derivitive_1.subs(s,0) # put in the point s=0
deriv_at_0_d2=second_deriv.subs(s,0) # put in the point s=0
deriv_at_0_d3=sd.subs(s,0)# put in the point s=0

print("E[Y]: ",deriv_at_0_d1)
print("E[Y^2]: ",deriv_at_0_d2)
print("E[Y^3]: ",deriv_at_0_d3)
