import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,1050,0.05)
def deffer(z,t):
    x,omega = z
    dy_dt = omega
    domega_dt = m*(1-x**2)*omega-x
    return dy_dt, domega_dt
y0 = 1
omega0 = 0.1
m = 0.4
z0=y0,omega0
sol = odeint(deffer,z0,t)
plt.plot(sol[:,1],sol[:,0])
plt.legent
plt.show