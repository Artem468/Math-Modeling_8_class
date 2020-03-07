import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

seconds_in_year = 365*24*60*60
seconds_in_day  = 24*60*60
years = 2

t = np.arange(0,years*seconds_in_year,seconds_in_day)

def PPC(z,t):
    
    (x_1,v_x_1, y_1,v_y_1,
    x_2,v_x_2,y_2,v_y_2,
    x_3,v_x_3,y_3,v_y_3) = z
     
    dxdt_1 = v_x_1
    dv_xdt_1 = -G * sun_mass * x_1 / (x_1**2 + y_1**2)**1.5
    dydt_1 = v_y_1
    dv_ydt_1 = -G * sun_mass * y_1 / (x_1**2 + y_1**2)**1.5
    
    dxdt_2 = v_x_2
    dv_xdt_2 = -G * sun_mass * x_2 /(x_2**2 + y_2**2)**1.5
    dydt_2 = v_y_2
    dv_ydt_2 = -G * sun_mass *y_2 /(x_2**2 + y_2**2)**1.5
    
    dxdt_3 = v_x_3
    dv_xdt_3 = -G * sun_mass * x_3 /(x_3**2 + y_3**2)**1.5
    dydt_3 = v_y_3
    dv_ydt_3 = -G * sun_mass *y_3 /(x_3**2 + y_3**2)**1.5
    
    return (dxdt_1,dv_xdt_1,dydt_1,dv_ydt_1,
             dxdt_2, dv_xdt_2,dydt_2,dv_ydt_2,
             dxdt_3, dv_xdt_3,dydt_3,dv_ydt_3)
    
x0_1 = 0.0 
v_x0_1 =  29163.96599832879
y0_1 = 149000000000.0 
v_y0_1 = 3.5715557610295594e-12

x0_2 = 18674651801.081333 
v_x0_2 = 28933.999415577557 
y0_2 = 147825090495.8572 
v_y0_2 =  -7252.783413404042

x0_3 =  37054793187.56336
v_x0_3 =  28247.726377709216 
y0_3 = 144318891008.16602
v_y0_3 = -7252.783413404042 

z0 = (x0_1,v_x0_1,y0_1,v_y0_1,
      x0_2,v_x0_2,y0_2,v_y0_2,
      x0_3,v_x0_3,y0_3,v_y0_3)

G = 6.67 * 10**(-11)
sun_mass = 1.9 * 10**30

sol = odeint(PPC,z0,t)

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    
    sun, = plt.plot([0], [0], 'yo', ms=10)
    
    p1, = plt.plot(sol[i, 0], sol[i,2], 'ro')
        
    p2, = plt.plot(sol[i,4], sol[i,6], 'bo')
    
    p3, = plt.plot(sol[i,8], sol[i,10], 'go')
   
    planets.append([sun,p1,p2])
   
ani = ArtistAnimation(fig,planets,interval = 50)
plt.axis('equal')
ani.save('neptun_plyton.gif')