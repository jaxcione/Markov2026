import numpy as np
import matplotlib.pyplot as plt
import random
import scipy

counter=0
matrix=[[9/10,1/10,0],[0,7/8,1/8],[2/5,0,3/5]]
p_50=np.linalg.matrix_power(matrix,50)
p_10000=np.linalg.matrix_power(matrix,10000)
print(p_50)
print()
print(p_10000)