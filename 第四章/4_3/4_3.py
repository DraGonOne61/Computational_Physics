# 单摆，摆长l=1.016m，重力加速度g=9.81m/s^2，摆球质量m=0.05kg，其受到阻力与速度成正比，比例系数为k=0.02
# 初始时，单摆由水平放置开始运动，取微小变化的位移ds，此时速度可表示为v=ds/dt，当ds足够小时，ds可表示为ds=l*dθ
# 那么此时摆球在运动方向上受到的阻力f=k*l*dθ/dt，受到的分力为F=mg*sinθ，则其微分方程为：
# m*l*d^2θ/dt^2+m*g*sinθ+k*l*dθ/dt=0
# 用二级欧拉近似法求解θ-t图像（0<t<25, dt=0.01）

import numpy as np
from matplotlib import pyplot as plt


m = 0.05
l = 1.016
g = 9.81
k = 0.02
t = 25
dt = 0.01
theta = np.zeros(int(t / dt) + 1, dtype=np.float64)
omega = np.zeros(int(t / dt) + 1, dtype=np.float64)
omega_1 = np.zeros(int(t / dt) + 1, dtype=np.float64)
theta[0] = 1
omega[0] = 0
omega_1[0] = 0
for i in range(int(t / dt)):
    f = -k * l * omega[i] - m * g * np.sin(theta[i])
    omega_1[i + 1] = omega[i] + f / (m * l) * dt
    f1 = -k * l * omega_1[i + 1] - m * g * np.sin(theta[i])
    omega[i + 1] = 0.5 * (omega[i] + omega_1[i + 1] + f1 / (m * l) * dt)
    theta[i + 1] = theta[i] + omega[i] * dt
file = open('pendulum.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(theta[i]) + ' ' + str(omega[i]) + '\n')
file.close()

file = open('pendulum.txt', 'r')
x, y, z = [], [], []
for line in file:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    z.append(float(line.split()[2]))
file.close()
plt.plot(x, y, label='theta')
plt.plot(x, z, label='omega')
plt.legend()
plt.savefig('pendulum.png')
