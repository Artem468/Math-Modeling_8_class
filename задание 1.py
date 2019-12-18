import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t= np.arange(0,5,0.1)
def bacteria(n,t):
       dmdt=n*k
       return dmdt
k=0.5
m=10
sove = odeint(bacteria,m,t)
plt.plot(t,sove[:,0])
plt.show