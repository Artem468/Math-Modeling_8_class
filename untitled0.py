import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0,3*np.pi,0.01)
x = 2**(-0.1*t)*np.cos(t)
y = 2**(-0.1*t)*np.sin(t)
z = -t
ax.plot(x,y,z)