# 一物体掉落，下落过程中，受到空气的阻力与下落速度平方成正比，正比系数K=0.05N*S/m，
# 重力加速度g=9.81m/s^2，物体质量m=50kg，设楼顶处为原点，初速度为0，
# 用一级欧拉近似法和二级欧拉近似法求解物体的x-t和v-t图像（0<=t<=3, dt=0.1）

import numpy as np
from matplotlib import pyplot as plt

m = 50
K = 0.05
g = 9.81
t = 3
dt = 0.1

# 一级欧拉近似法
y = np.zeros(int(t / dt) + 1, dtype=np.float64)
v = np.zeros(int(t / dt) + 1, dtype=np.float64)
y[0] = 0
v[0] = 0
for i in range(int(t / dt)):
    f = m * g - K * v[i] ** 2
    v[i + 1] = v[i] + f / m * dt
    y[i + 1] = y[i] + v[i] * dt
file = open('first_order_euler_approximation.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(v[i]) + ' ' + str(y[i]) + '\n')
file.close()

# 二级欧拉近似法
y = np.zeros(int(t / dt) + 1, dtype=np.float64)
v = np.zeros(int(t / dt) + 1, dtype=np.float64)
v_1 = np.zeros(int(t / dt) + 1, dtype=np.float64)
y[0] = 0
v[0] = 0
v_1[0] = 0
for i in range(int(t / dt)):
    f = m * g - K * v[i] ** 2
    v_1[i + 1] = v[i] + f / m * dt
    f1 = m * g - K * v_1[i + 1] ** 2
    v[i + 1] = 0.5 * (v[i] + v_1[i + 1] + f1 / m * dt)
    y[i + 1] = y[i] + v[i] * dt
file = open('second_order_euler_approximation.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(v[i]) + ' ' + str(y[i]) + '\n')
file.close()


def plot(file_name, title):
    _file = open(file_name, 'r')
    _x, _y, _v = [], [], []
    for line in _file:
        _x.append(float(line.split()[0]))
        _v.append(float(line.split()[1]))
        _y.append(float(line.split()[2]))
    _file.close()
    plt.title(title)
    plt.plot(_x, _v, label='v')
    plt.plot(_x, _y, label='y')
    plt.legend()
    plt.savefig(file_name.split('.')[0] + '.png')
    plt.clf()


plot('first_order_euler_approximation.txt', 'First Order Euler Approximation')
plot('second_order_euler_approximation.txt', 'Second Order Euler Approximation')
