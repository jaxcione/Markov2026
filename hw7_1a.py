import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import poisson

lamda_A=2
lamda_B=1.5

x=0
N=500
prob=0

for k in range(N):
    P_Y=poisson.pmf(k, lamda_B) #P(Y=k)
    P_X_to_k=poisson.cdf(k, lamda_A) #P(X<=k)
    prob+=P_Y*P_X_to_k

print(1-prob)