import numpy as np
import matplotlib.pyplot as plt

def a(x,y):
    return x+y

def b(x,y):
    return x*y

x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)

X, Y = np.meshgrid(x, y)
Z = a(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
cmap='jet', edgecolor='none')
ax.set_title('surface')
ax.set_xlabel('x', fontsize = 11)
ax.set_ylabel('y', fontsize = 11)
ax.set_zlabel('Z', fontsize = 10)
plt.show()

Z = b(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
cmap='jet', edgecolor='none')
ax.set_title('surface')
ax.set_xlabel('x', fontsize = 11)
ax.set_ylabel('y', fontsize = 11)
ax.set_zlabel('Z', fontsize = 10)
plt.show()

