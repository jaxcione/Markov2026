import numpy as np 

P = [[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1]]

eigenvals, eigenvect = np.linalg.eig(P) #obtaing eigen vals and vecs 
idx = np.argsort(eigenvals.real) #soring them by size 
eigenvals = eigenvals[idx]
eigenvect = eigenvect[:, idx]  
eigenvect = eigenvect / eigenvect[0, :] #normalizing

for i in range(len(eigenvals)): #printing so i can see them
    print(f"Eigenvalue: {eigenvals[i].real:.4f} + {eigenvals[i].imag:.4f}i")
    print(f"Eigenvector:")
    for component in eigenvect[:, i]:
        print(f"  {component.real:.4f} + {component.imag:.4f}i")

V =eigenvect   #eigenvec matrix
y0 = np.array([1/3, 2/3, 0, 0]) #intitial conditrion 
c = np.linalg.solve(V, y0) #coeff

print("Coefficients c_i:")
for i, ci in enumerate(c):
    print(f"  c{i+1} = {ci.real:.4f} + {ci.imag:.4f}i") #printing coeff
