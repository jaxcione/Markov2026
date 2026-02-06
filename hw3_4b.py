import numpy as np


P = np.array([
    [1/2, 1/2, 0,   0,   0, 0],
    [0,   1/2, 1/2, 0,   0, 0],
    [1/3, 0,   1/3, 1/3, 0, 0],
    [0,   0,   0,   1/2, 1/2, 0],
    [0,   0,   0,   0,   0, 1],
    [0,   0,   0,   0,   1, 0]
])

print(np.round(np.linalg.matrix_power(P, 10000), decimals=5))