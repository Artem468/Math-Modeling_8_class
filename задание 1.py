import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

#параболоид...
fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)

x = np.outer((phi), np.cos(theta))
y = np.outer((phi), np.sin(theta))
z = np.outer(phi**2, np.ones(np.size(theta)))

ax.plot_surface(x, y, z, color="b")
plt.show()

#гиперболид...
fig = plt.figure()
ax = p3.Axes3D(fig)

a = 3
b = 2
c = 5

phi = np.linspace(-2*np.pi, 2 * np.pi, 100)
theta = np.linspace(-2*np.pi, 2*np.pi, 100)

x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.outer(np.ones(np.size(phi)),np.sinh(theta))

ax.plot_surface(x, y, z, color="g")
plt.show()

#геликоид...
fig = plt.figure()
ax = p3.Axes3D(fig)

h = 2

phi = np.linspace(-2*np.pi, 2 * np.pi, 100)
theta = np.linspace(-2*np.pi, 2*np.pi, 100)

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * np.outer(np.ones(np.size(phi)), theta )

ax.plot_surface(x, y, z, color="y")
plt.show()

#коноид...

fig = plt.figure()
ax = p3.Axes3D(fig)

l = 2
f = 7
m = 4
n = 9

phi = np.linspace(-2*np.pi, 2 * np.pi, 100)
theta = np.linspace(-2*np.pi, 2*np.pi, 100)

x = np.outer(phi, np.cos(theta)) + l * np.outer(np.ones(np.size(phi)), theta**2)
y = np.outer(phi, np.sin(theta)) + m * f *np.outer(np.ones(np.size(phi)), theta)
z = n * f * np.outer(np.ones(np.size(phi)), theta) 

ax.plot_surface(x, y, z, color="r")
plt.show()