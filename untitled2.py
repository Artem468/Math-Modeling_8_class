import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0,4*np.pi,0.01)
x = np.sin(2*t)
y = 1-np.cos(2*t)
z = 2*np.cos(t)
ax.plot(x,y,z)