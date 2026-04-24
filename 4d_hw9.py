import numpy as np 
import matplotlib.pyplot as plt


vals=np.arange(1,1000)
B=1

sums=np.cumsum(1/vals)/B

y=np.log(vals)/B

plt.plot(vals,sums,linewidth=2,color="red",linestyle='dashed',label="Sum")
plt.plot(vals,y,linewidth=2,color="purple",label="ln")
plt.xlabel("m")
plt.ylabel("Tm")
plt.grid(True,alpha=.4)
plt.legend()
plt.show()