import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.01)
def dif(z, t):
    y, v= z
    dydt=v
    dvdt=-np.sin(y)*v-3*y*t-5
    return dydt, dvdt
y0=3
v0=0.5
z0=y0,v0
solv = odeint(dif, z0, t)
plt.plot(t, solv[:,1])
plt.show