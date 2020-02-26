import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

a = 0.008
q1 = 1.1 * 10**(-13)
q2 = -1.1 * 10**(-13)
q3 = 1.1 * 10**(-13)
q4 = -1.1 * 10**(-13)
K = 9*10**9
m1 = m2 = m3 = m4 = 1.1 * 10**(-27)

def dif_func(s, t):

    (x1, v_x1, y1, v_y1, 
     x2, v_x2, y2, v_y2, 
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4) = s
     
    dxdt1 = v_x1
    dv_xdt1 = (-K*q1*q2/m1* (x1-x2) / ((x1-x2)**2+(y1-y2)**2)**1.5
               -K*q1*q3/m1 * (x1-x3) / ((x1-x3)**2+(y1-y3)**2)**1.5
               -K*q1*q4/m1 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dydt1 = v_y1
    dv_ydt1 = (-K*q1*q2/m1* (y1-y2) / ((x1-x2)**2+(y1-y2)**2)**1.5
               -K*q1*q3/m1* (y1-y3) / ((x1-x3)**2+(y1-y3)**2)**1.5
               -K*q1*q4/m1* (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dxdt2 = v_x2
    dv_xdt2 = (-K*q2*q1/m2* (x2-x1) / ((x2-x1)**2+(y2-y1)**2)**1.5
               -K*q2*q3/m2*(x2-x3) / ((x2-x3)**2+(y2-y3)**2)**1.5
               -K*q1*q4/m2 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (-K*q2*q1/m2* (y2-y1) / ((x2-x1)**2+(y2-y1)**2)**1.5
               -K*q2*q3/m2* (y2-y3) / ((x2-x3)**2+(y2-y3)**2)**1.5
               -K*q1*q4/m2 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dxdt3 = v_x3
    dv_xdt3 = (-K*q3*q1/m3* (x3-x1) / ((x3-x1)**2+(y3-y1)**2)**1.5
                 -K*q3*q2/m3* (x3-x2) / ((x3-x2)**2+(y3-y2)**2)**1.5
                 -K*q1*q4/m3 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (-K*q3*q1/m3* (y3-y1) / ((x3-x1)**2+(y3-y1)**2)**1.5
                 -K*q3*q2/m3*(y3-y2) / ((x3-x2)**2+(y3-y2)**2)**1.5
                 -K*q1*q4/m3 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dxdt4 = v_x4
    dv_xdt4 = (-K*q4*q1/m4* (x4-x1) / ((x4-x1)**2+(y4-y1)**2)**1.5
                 - K*q4*q2/m4*(x4-x3) / ((x4-x3)**2+(y4-y3)**2)**1.5
                 -K*q1*q3/m1 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    dydt4 = v_y4
    dv_ydt4 = (-K*q4*q1/m4* (y4-y1) / ((x4-x1)**2+(y4-y1)**2)**1.5
                 -K*q4*q3/m4*(y4-y3) / ((x4-x3)**2+(y4-y3)**2)**1.5
                 -K*q1*q3/m1 * (x1-x4) / ((x1-x4)**2+(y1-y4)**2)**1.5)
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4)
    

t = np.arange(10**(-7),1.5*10**(-7), 10**(-9))

v = 4 * 10**6/(2**0.5)

x01 = -a
v_x01 = -  v
y01 = a
v_y01 = - v

x02 = a
v_x02 = - v
y02 = a
v_y02 = v

x03 = a
v_x03 = v
y03 = -a
v_y03 = v

x04 = -a
v_x04 = v
y04 = -a
v_y04 = - v

s_0 = (x01, v_x01, y01, v_y01,
       x02, v_x02, y02, v_y02,
       x03, v_x03, y03, v_y03,
       x04, v_x04, y04, v_y04)

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
    
    body4, = plt.plot(sol[:i, 12], sol[:i, 14], '-', color='y')
    body4_line, = plt.plot(sol[i, 12], sol[i, 14], 'o', color='y')
       
    bodys.append([body1, body1_line, 
                   body2, body2_line, 
                   body3, body3_line,
                   body4, body4_line])

ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('chto эto.gif')