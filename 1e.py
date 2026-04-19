import numpy as np 
import matplotlib.pyplot as plt

Q = [[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1]] #rate amtrix
P=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]] #transtion matrix
N=[100,1000,10000,100000]

eigenvals, eigenvect = np.linalg.eig(Q) #obtaing eigen vals and vecs 
idx = np.argsort(eigenvals.real) #soring them by size 
eigenvals = eigenvals[idx]
eigenvect = eigenvect[:, idx]  
eigenvect = eigenvect / eigenvect[0, :] #normalizing

V =eigenvect   #eigenvec matrix
y0 = np.array([1/3, 2/3, 0, 0]) #intitial conditrion 
c = np.linalg.solve(V, y0) #coeff

def simulate_cont(t_end,P):
    #simulating our IC. since we are in state 1 1/3 of the time  
    u=np.random.random()
    if u<1/3:
        current_state=0
    else:
        current_state=1

    t=0 #starting at time =0 
    times=[0]
    states=[current_state]#marking down which state we start in 

    while t<t_end:
        wait=np.random.exponential(1) #jumping is  ditributed exp. how long we stay in each state 
        t+=wait #how long we wait 
        if t>t_end: #if we are over the end time leve
            break
        
        current_state=(current_state+1)%4
        times.append(t)
        states.append(current_state)
    return times,states
def num_state1(times,states,t_ask):
    idx = np.searchsorted(times, t_ask, side='right') - 1 #got this alrogtihm online 
    return 1 if states[idx] == 0 else 0 #returns 1 if wee are in state 1

def theoretical_y1(t): #our theoretical
    part1=1/4
    part2=(0.083+0.1667j)*np.exp((-1 +1j)*t)
    part3=(0.083-0.1667j)*np.exp((-1-1j) *t)
    part4=-0.083*np.exp(-2*t)
    return(part1+part2+part3+part4).real

for k in N: #plotting for each N
    t_vals =np.linspace(0,5,50)
    num_1=np.zeros(len(t_vals))
    for _ in range(k):
        times, states=simulate_cont(5, Q)
        for i, t in enumerate(t_vals):
            num_1[i]+=num_state1(times, states, t) #getting to see how many n=1 terms we have 
    num_1/= k #getting the fraction by dividing over the length of iterations we are running (k)
    theoretical =[theoretical_y1(t) for t in t_vals]

    plt.figure()
    plt.plot(t_vals, num_1, label='simulation',color="purple")
    plt.plot(t_vals, theoretical, label='theoretical', linestyle='--',color="green")
    plt.axhline(y=1/4, color='black', linestyle=':', label='π=1/4')
    plt.ylim(0, 1/2) #limits enforced by prob
    plt.xlim(0, 5)#limits enforced by prob
    plt.title(f'Probability of being in State 1, N={k} chains')
    plt.xlabel('time')
    plt.legend()
    plt.show()