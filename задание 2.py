import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 50, 0.1)
def dif(n, t):
    s, v = n
    dsdt=v
    dwdt=-g*np.sin(s/l)-k/m*v
    return dsdt,dwdt
g=9.81
l = 4
k = 1
m = 10

s0 = 2
v0 = 2
n0 = s0, v0

sove=odeint(dif, n0, t)

plt.plot(t, sove[:,0])
plt.show()