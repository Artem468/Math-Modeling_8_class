import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

G = 6.67 * 10**(-11)
AE = 149.6 * 10**(9)
M1 = 0.6 * (1.98847 * 10**(30))
M2 = 0.3 * (1.98847 * 10**(30))
M3 = 1.06 * (1.98847 * 10**(30)) 

def dif_func(s, t):

    (x1, v_x1, y1, v_y1, 
     x2, v_x2, y2, v_y2, 
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4) = s
     
    dxdt1 = v_x1
    dv_xdt1 = (- G*M2*(x1-x2) / ((x1-x2)**2+(y1-y2)**2)**1.5
            -  G*M3*(x1-x3) / ((x1-x3)**2+(y1-y3)**2)**1.5)
    dydt1 = v_y1
    dv_ydt1 = (- G*M2*(y1-y2) / ((x1-x2)**2+(y1-y2)**2)**1.5
               - G*M3*(y1-y3) / ((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dxdt2 = v_x2
    dv_xdt2 = (- G*M1*(x2-x1) / ((x2-x1)**2+(y2-y1)**2)**1.5
               - G*M3*(x2-x3) / ((x2-x3)**2+(y2-y3)**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (- G*M1*(y2-y1) / ((x2-x1)**2+(y2-y1)**2)**1.5
                 - G*M3*(y2-y3) / ((x2-x3)**2+(y2-y3)**2)**1.5)
    
    dxdt3 = v_x3
    dv_xdt3 = (- G*M1*(x3-x1) / ((x3-x1)**2+(y3-y1)**2)**1.5
                 - G*M2*(x3-x2) / ((x3-x2)**2+(y3-y2)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (- G*M1*(y3-y1) / ((x3-x1)**2+(y3-y1)**2)**1.5
                 -G*M2*(y3-y2) / ((x3-x2)**2+(y3-y2)**2)**1.5)
    
    dxdt4 = v_x4
    dv_xdt4 = (- G*M1*(x4-x1) / ((x4-x1)**2+(y4-y1)**2)**1.5)
    dydt4 = v_y4
    dv_ydt4 = (- G*M1*(y4-y1) / ((x4-x1)**2+(y4-y1)**2)**1.5)
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4)
    
sec_in_year = 60 * 60 * 24 * 365
sec_in_day = 24 * 60 * 60
years = 15
t = np.arange(0, years*sec_in_year, sec_in_day*5)

x0a = -8.3 * AE
v_x0a = 0
y0a = 0
v_y0a = 10000

x0b = 0* AE
v_x0b = 0
y0b = 0
v_y0b = 18000 

x0c = 4* AE
v_x0c = 0
y0c = 0
v_y0c = 15000 

x0d = 
v_x0d = 
y0d = 
v_y0d = 

s_0 = (x0a, v_x0a, y0a, v_y0a,
       x0b, v_x0b, y0b, v_y0b,
       x0c, v_x0c, y0c, v_y0c)

sol = odeint(dif_func, s_0, t)
fig = plt.figure()
bodys = []
for i in range(len(t)):
    body1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='g')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='g')
    
    body2, = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='r')
    body2_line, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='r')
    
    body3, = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='k')
    body3_line, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='k')
       
    bodys.append([body1, body1_line, 
                   body2, body2_line, 
                   body3, body3_line])

ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('chto_to.gif')