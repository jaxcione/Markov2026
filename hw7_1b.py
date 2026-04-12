import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import poisson

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import poisson

lambda_A=2/90
lambda_B=1.5/90

x=0
N=500
prob=[]
t=np.linspace(0,90,100)

def P(t):
    prob = 0
    for k in range(N):
        P_x=poisson.pmf(k, lambda_A*(90-t))
        P_y=poisson.pmf(k, lambda_B*(90-t)) #P(Y=k)
        prob += P_x*P_y
    return prob

def rest(t):      
    P_y2 = poisson.pmf(1, lambda_B * (90 - t))    #1 B goal
    P_x2 = poisson.pmf(0, lambda_A * (90 - t))    #no A goals
    return P_x2  * P_y2

def full(t):
    result = np.where(t<=60,P(t),rest(t))
    return result

plt.plot(t,full(t),color='purple',label="P(Tie|T=t)")
plt.xlabel('t')
plt.axvline(x=60, color='red', linestyle='--', label='A scores at t=60')  
plt.ylabel('P(X=Y|T=t)')
plt.title('P(X=Y|T=t) vs t')
plt.legend()
plt.show()
