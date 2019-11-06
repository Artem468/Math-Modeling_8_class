import matplotlib.pyplot as plt
import numpy as np
def parabollagiperbola(a=1,b=1,c=1):
    x=np.arange(-10,10,0.01)
    y=a*x**2 + b*x+c
    plt.plot(x,y,label="парабола и гипербола")
    plt.legend()
    plt.show()

parabollagiperbola()