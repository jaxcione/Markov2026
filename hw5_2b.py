import numpy as np

K=.1
a=.04
b=.16
p = lambda n:K*np.exp(a*n)
q = lambda n:K*np.exp(b*(n -1))
p1,p2,p3,p4=p(1),p(2),p(3),p(4)
q2,q3,q4,q5=q(2),q(3),q(4),q(5)

P =np.array([
    [1-p1,    p1,       0,       0,    0],
    [q2,  1-p2-q2,     p2,       0,    0],
    [0,       q3,  1-p3-q3,     p3,    0],
    [0,        0,      q4,  1-p4-q4,  p4],
    [0,        0,       0,      q5,  1-q5]])

eigenvalues, eigenvectors = np.linalg.eig(P.T) #tranposed P eigen values and eigen vectors 

for i in range(len(eigenvalues)):
    if abs(eigenvalues[i]-1) <1e-10: #if the eigenvalue is close to 1, we found the stationary distribution
       j=i #just storing what index its at 
       stat_dist=(eigenvectors[:,i].real)/(eigenvectors[:,i].sum()) #normalize the eigenvector (note its in a form of a matrix A=[e1 e2,e3...] so grab the column) to get the stationary distribution

check=np.matmul(P.T,stat_dist) #seeing if P*pi=pi 

print(f"Stationary distribution:{j}", stat_dist)
print(check)