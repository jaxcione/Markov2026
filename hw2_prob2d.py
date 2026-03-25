import numpy as np
import random
import time
import matplotlib.pyplot as plt
import sympy 
import scipy

start=time.time()
storage=[]
while len(storage)<10**6:
    u=np.random.exponential(1)
    z=np.random.exponential(1)
    storage.append(u+z)


end=time.time()
print(f"Total Run Time: {end-start}")

