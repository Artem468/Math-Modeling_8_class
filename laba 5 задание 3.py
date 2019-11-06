import matplotlib.pyplot as plt
import numpy as np
def nyb(R=1, A=2, B=1):
    x=np.arange(-2,2,0.1)
    y=np.arange(-2,2,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
    fxy2=X**2/A**2+Y**2/B**2
    plt.contour(X,Y,fxy2,levels=[1])
    plt.show()
    
nyb(3)

