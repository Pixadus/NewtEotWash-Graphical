import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig = plt.figure()

n = 64
xs = np.linspace(-5, 5, n)
ys = np.linspace(-5, 5, n)
#s.plot_surface(mxs, mys, np.zeros_like(zs))

s1 = fig.add_subplot(111, projection="3d")

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

r, h = 5, 4
zs = np.array([max(h * (1 - np.hypot(x, y) / r), 0)
               for x in xs for y in ys]).reshape((n, n))

mxs, mys = np.meshgrid(xs, ys)

# Plot the surface.
X += 10
Y += 10
Z+=0.1
surf = s1.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
surf1 = s1.plot_surface(mxs, mys, zs)


# Customize the z axis.
s1.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
s1.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
