import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig=plt.figure()
x = np.linspace(-6,6,100)
a=10
b=20
c=5
y = a*x**2+b*x+c
anim_list = []
for i in range(0,100,1):
    anime, = plt.plot(x[:i], y[:i],"-", color="r")
    anime2, = plt.plot(x[i], y[i],"o", color="r")
    anim_list.append([anime,anime2])
anni = ArtistAnimation(fig, anim_list, interval=50)

anni = ArtistAnimation(fig, anim_list, interval=50)
anni.save("aani.gif")