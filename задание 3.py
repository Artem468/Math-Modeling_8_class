import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 2

t = np.arange(0, years*seconds_in_year, seconds_in_day)

def grav_func(z, t):
    (x_mars, v_x_mars, y_mars, v_y_mars,
     x_saturn, v_x_saturn, y_saturn, v_y_saturn) = z
     
    dxdt_mars = v_x_mars
    dv_xdt_mars = -G * sun_mass * x_mars / (x_mars**2 + y_mars**2)**1.5
    dydt_mars = v_y_mars
    dv_ydt_mars = -G * sun_mass * y_mars / (x_mars**2 + y_mars**2)**1.5
     
    dxdt_saturn = v_x_saturn
    dv_xdt_saturn = -G * sun_mass * x_saturn / (x_saturn**2 + y_saturn**2)**1.5
    dydt_saturn = v_y_saturn
    dv_ydt_saturn = -G * sun_mass * y_saturn / (x_saturn**2 + y_saturn**2)**1.5
     
    return (dxdt_mars, dv_xdt_mars, dydt_mars, dv_ydt_mars,
            dxdt_saturn, dv_xdt_saturn, dydt_saturn, dv_ydt_saturn)

G = 6.67 * 10**(-11)
sun_mass = 1.989 * 10**30

x0_mars = 228000000000
v_x0_mars = 0 
y0_mars = 0
v_y0_mars = 24130

x0_saturn=1433449370000
v_x0_saturn=0
y0_saturn=0
v_y0_saturn=9690

z0 = (x0_mars, v_x0_mars, y0_mars, v_y0_mars, 
      x0_saturn, v_x0_saturn, y0_saturn, v_y0_saturn)

sol = odeint(grav_func, z0, t)

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    sun, = plt.plot([0], [0], "o", ms=10)
    
    mars, = plt.plot(sol[:i, 0], sol[:i, 2], "r-")
    mars_line, = plt.plot(sol[i, 0], sol[i, 2], "ro")
    
    saturn, = plt.plot(sol[:i, 4], sol[:i, 6], "b-")
    saturn_line, = plt.plot(sol[i, 4], sol[i, 6], "bo")
    
    planets.append([sun,mars,mars_line, saturn, saturn_line])

ani = ArtistAnimation(fig, planets, interval=50)
plt.axis("equal")
ani.save("mars_saturn.gif")