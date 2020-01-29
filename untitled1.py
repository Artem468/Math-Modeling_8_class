import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0,4*np.pi,0.01)
R = 1
x = R*np.cos(t)**3
y = R*np.sin(t)**3
z = np.cos(2*t)
ax.plot(x,y,z)