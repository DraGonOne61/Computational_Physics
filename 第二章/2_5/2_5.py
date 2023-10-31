import numpy as np
from matplotlib import pyplot as plt

dx = 0.5
x = np.arange(-9, 9 + dx, dx)
y = np.arange(-9, 9 + dx, dx)
X, Y = np.meshgrid(x, y)
C = 2.77
A = 1
Uc = C * (np.log(A / np.sqrt((X + 2) ** 2 + Y ** 2)) - np.log(A / np.sqrt((X - 2) ** 2 + Y ** 2)))
Ex, Ey = np.gradient(-Uc, dx, dx)
plt.contour(X, Y, Uc, 25)
plt.axis([-9, 9, -9, 9])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('2_5.png')