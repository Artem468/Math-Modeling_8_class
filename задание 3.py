import numpy as np
from konstant import g
t = np.arange(0,5,0.01)
n=len(t)
x0 = 5
y0 = 7
v = 6

N=len(t)
B= np.ndarray((N,3))
for i in range(0,N,1):
    x = x0+v*t[i]
    y= y0+v*t[i]- g*t[i]**2/2
    
    B[i, 0] = t[i]
    B[i,1] = x
    B[i, 2] =y
print (B)                                                               