import numpy as np

def massiv(a):
    f=1
    for i in range(0, len(a), 1):
        f=f*a[i]
    print(f)
    
f=np.arange(2,6,2)
massiv(f)