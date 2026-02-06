import numpy as np
import random


matrix=[[1,0,0,0,0],[1/3,0,2/3,0,0],[0,1/3,0,2/3,0],[0,0,1/3,0,2/3],[0,0,0,0,1]]
p_4=np.linalg.matrix_power(matrix,50)
print(np.round(p_4, decimals=5))