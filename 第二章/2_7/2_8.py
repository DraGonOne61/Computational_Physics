import matplotlib.pyplot as plt
import numpy as np

N = 500
a = 1e-3
d = 2e-3
lamda = 0.59
k = 2 * np.pi / lamda
theta = np.arange(20, 60, 0.1)
I = []
for i in theta:
    I.append((np.sin(N * k * a * np.sin(i) / 2) / np.sin(k * a * np.sin(i) / 2)) ** 2 * (
            np.sin(N * k * d * np.sin(i) / 2) / np.sin(k * d * np.sin(i) / 2)) ** 2)
plt.plot(theta, I)
plt.xlabel('theta')
plt.ylabel('I')
plt.savefig('2_8.png')
