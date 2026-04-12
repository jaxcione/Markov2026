import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp   
import statistics


lamb=3 #rate 3/min
t_i=0 #initial time
t_f=48 #final time
teamA_scored=[] #initializing list to store the times when team A scored
teamB_scored=[]    #initializing list to store the times when team B scored
Num_simulations=1E5# number of simulations to run
numtie=[]
D=[]

for i in range(int(Num_simulations)):
        N=np.random.poisson(2*lamb*t_f) #number of goals scored in the game, drawn from a poisson distribution with mean lamb*t_f
        N_a_givenN=np.random.binomial(N, 0.5) #number of goals scored by team A given N total goals, drawn from a binomial distribution with p=0.5
        N_b_givenN=N-N_a_givenN #number of goals scored by team B given
        d=2*(N_a_givenN-N_b_givenN) #calculating D for this simulation
        if d==0: #if the number of goals scored by team A and team B are equal--> tie
                numtie.append(1)
        else:
                numtie.append(0)
        D.append(d)


print(f'Probability of a tie: {statistics.mean(numtie)}')
print(f'Expected value of D: {statistics.mean(D)}')
print(f'Variance of D: {statistics.variance(D)}')
print("-------------------------------------------------------")
#theoretical
print("Theoretical probability of a tie:",1/np.sqrt(4*np.pi*lamb*t_f))
print("Theoretical expected value:",0)
print("Theoretical variance:",8*lamb*t_f)


