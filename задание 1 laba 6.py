import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-2*np.pi,10*np.pi,0.1)
R=3
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,linestyle="-",linewidth=5)
plt.axis('equal')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
R=15
t=np.arange(1,10,0.01)
x=R*np.cos(t)**3
y=R*np.sin(t)**3
plt.plot(x,y,label="xren")
plt.show()