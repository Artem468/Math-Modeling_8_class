import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

fig, ax = plt.subplots()

gh, = plt.plot([],[],'o')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
x, y = [], []
R=3

def asteroida_animate(t):
    x.append(R*np.cos(t)**3)
    y.append(R*np.sin(t)**3)
    gh.set_data(x,y)

ani = FuncAnimation(fig,
                  asteroida_animate,
                  frames=np.arange(0, 2*np.pi, 0.1), 
                  interval=100)

ani.save('anlhi.gif')
