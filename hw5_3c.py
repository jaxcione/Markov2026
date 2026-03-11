import numpy as np
import statistics
import sympy as sp
import matplotlib.pyplot as plt

a=.32

P=np.array([[1-a, a, 0], [a, 0, 1-a], [0, 1-a, a]]) 
A=P.T #transposing
eigenvalues,eigenvectors=np.linalg.eig(A) #obtaining eigen vals
#sorting eigen values cuz apparently numpy doesnt do that for u

idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

q0=[1,0,0] #initial state vector
V_inv=np.linalg.inv(eigenvectors) #inerse of the eigenvector matrix to find coefficients of the initial distribution in the eigenvector basis
coeff_c_vec=np.matmul(np.linalg.inv(eigenvectors),q0) #solving for coefff

for j in range(3): #just showing me everything at once
    print(f"c{j+1}:{coeff_c_vec[j]:.6f},lambda{j+1}: {eigenvalues[j]:.6f},v{j+1}:{eigenvectors[:, j]}")

#normalizing first tern
pi =coeff_c_vec[0]*eigenvectors[:, 0]
pi=pi/ pi.sum()
print("\nStationary distribution π:",pi)
print("Sum",pi.sum())