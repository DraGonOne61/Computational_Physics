# 半径为R的球形水罐，由底部半径为r的小孔排水，罐的顶部有孔，空气可以进入，求h-t关系
# 当水面高度为h时，水的体积为V=PI*h^2*(3*R-h)/3（1）
# 体积变化率为dV/dt=-A*v（2）
# 其中A为排水小孔的截面积，v是通过此面积的水流速度，式（2）还可写成
# dV/dt=-A*sqrt(2*g*h)（3）
# 式中g为重力加速度。若对式（1）求导，得
# dV/dt=（2*PI*R*h-PI*h^2）*dh/dt（4）
# 将式（3）和式（4）相等，得
# dh/dt=-r^2*sqrt(2*g*h)/（2*R*h-h^2）（5）
# 已知R=3.5，r=0.04，g=9.81，h=6.9，取步长delta_t=7.5s（当h=2*R时，（5）式分母为0）
# 用龙格库塔法求解（5）式，得到h-t关系（当罐快空时，即可停止计算。而当h小到一定程度时，（5）式分母也会趋近于0，此时步长应该减小）

import numpy as np
from matplotlib import pyplot as plt

g = 9.81
R = 3.5
r = 0.04
h = 6.9
dt = 7.5
t = 0
h_list = []
t_list = []
h_list.append(h)
t_list.append(t)
while h > 0.1:
    k1 = -r ** 2 * np.sqrt(2 * g * h) / (2 * R * h - h ** 2)
    k2 = -r ** 2 * np.sqrt(2 * g * (h + k1 * dt / 2)) / (2 * R * (h + k1 * dt / 2) - (h + k1 * dt / 2) ** 2)
    k3 = -r ** 2 * np.sqrt(2 * g * (h + k2 * dt / 2)) / (2 * R * (h + k2 * dt / 2) - (h + k2 * dt / 2) ** 2)
    k4 = -r ** 2 * np.sqrt(2 * g * (h + k3 * dt)) / (2 * R * (h + k3 * dt) - (h + k3 * dt) ** 2)
    h += (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
    t += dt
    h_list.append(h)
    t_list.append(t)
file = open('tank.txt', 'w')
for i in range(len(h_list)):
    file.write(str(t_list[i]) + ' ' + str(h_list[i]) + '\n')
file.close()

file = open('tank.txt', 'r')
x, y = [], []
for line in file:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
file.close()
plt.plot(x, y)
plt.savefig('tank.png')
