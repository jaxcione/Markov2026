import numpy as np
import statistics
import matplotlib.pyplot as plt

#given values
K=.1
a=.04
b=.16
p = lambda n:K*np.exp(a*n)
q = lambda n:K*np.exp(b*(n -1))
N=10**6
p1,p2,p3,p4=p(1),p(2),p(3),p(4)
q2,q3,q4,q5=q(2),q(3),q(4),q(5)

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

  #Fraction of times we go to each state
    # Prob_state1=state.count(0)/(len(state))
    # Prob_state2=state.count(1)/(len(state))
    # Prob_state3=state.count(2)/(len(state))
    # Prob_state4=state.count(3)/(len(state))
    # Prob_state5=state.count(4)/(len(state))
    # frac_vec=[Prob_state1,Prob_state2,Prob_state3,Prob_state4,Prob_state5]

    return state #returning the vector 

random_IC=np.random.choice(5) #random 
vals=simulate(random_IC,P) #grabing all the states
plt.hist(vals,density=True,bins=[-.5,.5,1.5,2.5,3.5,4.5],color="skyblue",edgecolor="black")#normalized hist
plt.xticks([0,1,2,3,4], ["State 1","State 2","State 3","State 4","State 5"])
plt.xlabel("States")
plt.ylabel("Frequency")
plt.show()