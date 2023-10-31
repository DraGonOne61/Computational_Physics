# 用龙格库塔法计算4_2中阻尼震动方程的解

import numpy as np
from matplotlib import pyplot as plt


def runge_kutta(_beta, _omega0, _t, _dt):
    _x = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _v = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _x[0] = 1
    _v[0] = 0
    for i in range(int(_t / _dt)):
        k1 = _v[i]
        l1 = -2 * _beta * _v[i] - _omega0 ** 2 * _x[i]
        k2 = _v[i] + 0.5 * _dt * l1
        l2 = -2 * _beta * (k1 + 0.5 * _dt * l1) - _omega0 ** 2 * (_x[i] + 0.5 * _dt * k1)
        k3 = _v[i] + 0.5 * _dt * l2
        l3 = -2 * _beta * (k2 + 0.5 * _dt * l2) - _omega0 ** 2 * (_x[i] + 0.5 * _dt * k2)
        k4 = _v[i] + _dt * l3
        l4 = -2 * _beta * (k3 + _dt * l3) - _omega0 ** 2 * (_x[i] + _dt * k3)
        _x[i + 1] = _x[i] + _dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        _v[i + 1] = _v[i] + _dt / 6 * (l1 + 2 * l2 + 2 * l3 + l4)
    return _x, _v


omega0 = 1
t = 100
dt = 0.5

beta = 0.1
x, v = runge_kutta(beta, omega0, t, dt)
file = open('damper_vibration_1.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()

beta = 0.4
x, v = runge_kutta(beta, omega0, t, dt)
file = open('damper_vibration_2.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
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


plot('damper_vibration_1.txt', 'beta=0.1')
plot('damper_vibration_2.txt', 'beta=0.4')
