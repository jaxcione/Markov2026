import numpy as np
import statistics
import sympy as sp
import matplotlib.pyplot as plt

a=sp.symbols('a') #using symbolic math to find the eigenvalues and eigenvectors of the transition matrix P

P=sp.Matrix([[1-a, a, 0], [a, 0, 1-a], [0, 1-a, a]]) 
A=P.T #transposing
eigenvalues=sp.Matrix(A).eigenvals() #obtaining eigen vals
eigenvectors=sp.Matrix(A).eigenvects() #obtaining eigen vectors
for val, mult, vects in A.eigenvects():
    print(f"Eigenvalue: {val}")
    for v in vects:
        print("Eigenvector:")
        sp.pprint(v)
    print()