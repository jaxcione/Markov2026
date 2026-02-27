import numpy as np

A = np.array([
    [1, 0, 0, 0, 0],
    [-0.18, 0.1899, 0, 0, 0],
    [-0.027, -0.243, 0.247, 0, 0],
    [-0.0035, -0.048, -0.295, 0.3439, 0],
    [-0.0045, -0.0081, -0.0728, -0.328, 0.4095]
])

b = np.array([10, 1, 1, 1, 1])
e = np.linalg.solve(A, b)
for i, val in enumerate(e, 1):
    print(f"e{i} = {val:.4f}")