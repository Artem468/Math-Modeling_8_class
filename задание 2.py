import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def money(n,t):
       dndt = -n*k*t
       return dndt

k = 0.08
n0=1000

sove=odeint(money, n0, t)
plt.plot(t,sove[:,0])
plt.show()