import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,100,1)
def zto(v,t):
       dvdt = (F - y*v**2)/m
       return dvdt
v0 = 0
y = 0.01
m = 1
F=0.1
sove = odeint(zto,v0,t)
plt.plot(t,sove[:,0])
plt.show()