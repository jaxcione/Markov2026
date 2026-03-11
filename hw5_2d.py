import numpy as np
import statistics
import matplotlib.pyplot as plt
from itertools import product

#given values
K=.1
a=.04
b=.16
p = lambda n:K*np.exp(a*n)
q = lambda n:K*np.exp(b*(n -1))
N=10**6
p1,p2,p3,p4=p(1),p(2),p(3),p(4)
q2,q3,q4,q5=q(2),q(3),q(4),q(5)

pi_1=(1+(p1/q2)+(p1*p2)/(q2*q3)+(p1*p2*p3)/(q2*q3*q4)+(p1*p2*p3*p4)/(q2*q3*q4*q5))**(-1)

#our transtion matrix
P =np.array([ 
    [1-p1,    p1,       0,       0,    0],
    [q2,  1-p2-q2,     p2,       0,    0],
    [0,       q3,  1-p3-q3,     p3,    0],
    [0,        0,      q4,  1-p4-q4,  p4],
    [0,        0,       0,      q5,  1-q5]])

#simulating a markov chain
def simulate(init_state,P):
    state=[init_state] #creating an array of all the states we enter
    current_state=init_state

    for _ in range(N): #runnign this N times
        next_state=np.random.choice(len(P),p= P[current_state]) #what this does it picks a random number from [0,1,...,n-1] in this case len(P) is 5. And P[i] grabs the row
        state.append(next_state) # storing it in state so I can later calcualte Pi
        current_state=next_state #our next state is noow our current

    return state #returning the vector 

eigenvalues, eigenvectors = np.linalg.eig(P.T) #tranposed P eigen values and eigen vectors 

for i in range(len(eigenvalues)):
    if abs(eigenvalues[i]-1) <1e-10: #if the eigenvalue is close to 1, we found the stationary distribution
       j=i #just storing what index its at 
       stat_dist=(eigenvectors[:,i].real)/(eigenvectors[:,i].sum()) #normalize the eigenvector (note its in a form of a matrix A=[e1 e2,e3...] so grab the column) to get the stationary distribution


def theoretical_i(int_pick):

    numerator=np.prod([p(i) for i in range(1,int_pick)])
    denominator=np.prod([q(j) for j in range(2,int_pick+1)])

    return float(pi_1*(numerator/denominator))


pi_vec=[float(pi_1),theoretical_i(2),theoretical_i(3),theoretical_i(4),theoretical_i(5) ]   
print(pi_vec)

random_IC=np.random.choice(5) #random 
vals=simulate(random_IC,P) #grabing all the states

labels = ["State 1","State 2","State 3","State 4","State 5"]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#Simulated
axes[0].hist(vals, density=True, bins=[-.5,.5,1.5,2.5,3.5,4.5], color="purple", edgecolor="black")
axes[0].set_xticks([0,1,2,3,4], labels)
axes[0].set_title("Simulated")
axes[0].set_ylabel("Frequency")
#Theoretical
axes[1].bar([0,1,2,3,4], pi_vec, color="skyblue", edgecolor="black")
axes[1].set_xticks([0,1,2,3,4], labels)
axes[1].set_title("Theoretical")
#Eigenvector
axes[2].bar([0,1,2,3,4], stat_dist, color="red", edgecolor="black")
axes[2].set_xticks([0,1,2,3,4], labels)
axes[2].set_title("Eigenvector")
plt.tight_layout()
plt.show()