import numpy as np
from math import factorial

this=0
for i in range(0,1000):
    denom = np.prod([1+.083333*k for k in range(1,i+1)])
    this+=((1/2**i)/(denom))

print(this)

print(1/this)
print(60*(1-(1/this)))