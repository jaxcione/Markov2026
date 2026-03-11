import numpy as np
import statistics
import sympy as sp
import matplotlib.pyplot as plt

a=.99
i_s=0 #intial state

P=np.array([[1-a, a, 0], [a, 0, 1-a], [0, 1-a, a]]) 
A=P.T #transposing
eigenvalues,eigenvectors=np.linalg.eig(A) #obtaining eigen vals

#sorting eigen values cuz apparently numpy doesnt do that for u
index_sorted=np.argsort(eigenvalues)[::-1]
eigenvalues=eigenvalues[index_sorted]
eigenvectors=eigenvectors[:,index_sorted]
n_steps=300
n_vals=np.arange(0, n_steps+1)    

q0=[1,0,0] #initial state vector
V_inv=np.linalg.inv(eigenvectors) #inerse of the eigenvector matrix to find coefficients of the initial distribution in the eigenvector basis
coeff_c_vec=np.matmul(np.linalg.inv(eigenvectors),q0) #solving for coefff


#theroetical q_n(1) values using the eigen decomposition of the transition matrix(calculated above)
def q_n_theoretical(n_vals):
    result=[]
    for n in n_vals:
        qn = sum(coeff_c_vec[j] * eigenvalues[j]**n * eigenvectors[:, j] for j in range(3)) #3 cuzwe have 3 eigen values and eigen vectors
        result.append(qn[0]) #we only want the first element of the resulting vector since we are looking for q_n(1)
    return np.array(result)
theoretical = q_n_theoretical(n_vals)

#simulating N number of markov chains(same logic in problem 2c code)
def markov_chain(P,int_state,N,n_steps=300):
    state=np.full(N,int_state) #creating an array of all the states we enter starting at 1 of length N 
    current_state=np.full(N,int_state) #our current state is also 1 at the start
    num1_frac=[]
    for _ in range(n_steps): #running the markov chain for 300 steps, otherwise it takes too long to run for N=10000
        next_states=np.array([np.random.choice(len(P),p=P[m]) for m in current_state]) #what this does it picks a random number from [0,1,...,n-1] for each state in current_state
        state=np.append(state, next_states)
        current_state=next_states
        num1_frac.append(current_state.tolist().count(0)/(len(current_state))) #calculating the fraction of times we go to state 1 in our current vector 
    return num1_frac

N_vals=[100,1000,10000] #N vals we want to simulate for
for N in N_vals:
    f_n = markov_chain(P, i_s,N,n_steps) #simulating this markov chain for each N value and running the markov chain for 300 steps 
    plt.plot(range(1, n_steps+1), f_n, label=f'N={N}') #for each val in N we plot the fraction of times we go to state 1 as a function of n steps. We also label it with the N value for the legend

plt.plot(n_vals, theoretical,'k--', linewidth=2, label='Theoretical $q_n(1)$')
plt.axhline(y=1/3, color='r', linestyle="--", linewidth=2, label='Stationary Dist=1/3') #stationary distribution line 
plt.xlabel(" Number of Iterations")
plt.ylabel("Fraction in state 1")
plt.legend()
plt.show()