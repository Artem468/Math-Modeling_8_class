import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
r = 100
N = 10

def cd (r, N, v):
    for  i in range (0, N, 1):
         al = 2*np.pi/N
         x = np.cos(al * i) * r
         y = np.sin(al * i) * r
         if x<0 and y<0: 
             vx = v*np.cos(0.5*np.pi-al*i)
             vy= -v*np.sin(0.5*np.pi-al*i)
         elif x<0 and y>0:
            vx = v*np.sin(al*i)
            vy = -v*np.cos(al*i)
         else:
            vx = 0
            vy = 0
         plt.arrow(x, y, vx, vy)
         plt.scatter(x, y)
         plt.plot(x, y, marker="o")
    plt.axis("equal")
    plt.show()
cd (1, 150, 1)