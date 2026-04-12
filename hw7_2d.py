import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp   
import statistics


lamb=3 #rate 3/min
t_i=0 #initial time
t_f=48 #final time
teamA_scored=[] #initializing list to store the times when team A scored
teamB_scored=[]    #initializing list to store the times when team B scored

while True:
    dt=(np.random.exponential(1/lamb)) #time until next goal is scored, drawn from an exponential distribution with rate lamb
    t_i+=dt #increment the time by the time until the next goal
    if t_i>t_f:
        break
    np.random.random()
    if np.random.random()<0.5: #assuming each team has an equal chance of scoring P=1/2
        teamA_scored.append(t_i)
    else:
        teamB_scored.append(t_i)

#plotting 
fig, ax=plt.subplots(figsize=(12, 3))
ax.vlines(teamA_scored, ymin=0, ymax=1, label=f'Team A({len(teamA_scored)} baskets)',color='crimson',linewidth=1.5,alpha=0.8)
ax.vlines(teamB_scored, ymin=0, ymax=1, label=f'Team B ({len(teamB_scored)} baskets)',color='steelblue',linewidth=1.5,alpha=0.8)
ax.set_xlabel('Time (minutes)')
ax.set_title('Goals Scored Over Time')
ax.set_yticks([])
ax.set_xlim(0, t_f)
for spine in ['top','left', 'right']:
    ax.spines[spine].set_visible(False)
ax.legend()
plt.tight_layout()
plt.show()
