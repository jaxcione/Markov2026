import numpy as np
import math

def Poission(num):
    lamda=100*.98
    return(lamda**(num)*math.exp(-lamda)/(math.factorial(num)))

print(Poission(99)+Poission(100),"Poisson")
print(Poission(98)/((Poission(99)+Poission(100)+Poission(100))))


def Binomial(trials,prob,k):
    return(math.comb(trials,k)*(prob**k)*(1-prob)**(trials-k))
print(Binomial(100,.98,99)+Binomial(100,.98,100),"Binomial")


