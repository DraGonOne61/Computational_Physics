# 弹簧振子阻尼运动的方程为：
# d^2x/dt^2+2βdx/dt+ω0^2x=0 (β < ω0)
# ω0 = 1、t = 0时，x = 1、v = 0，delta_t = 0.5
# 分别取β = 0.1、0.4，用二级欧拉近似法求解x-t和v-t图像（0 < t < 100）

# 若是受迫振动，即微分方程为：
# d^2x/dt^2+2βdx/dt+ω0^2x=sin(ωt) (β < ω0)
# 求解ω = 0.5、1、2时的x-t图像（0 < t < 100）

import numpy as np
from matplotlib import pyplot as plt


# 阻尼振动
def damped_vibrations(_beta, _omega0, _t, _dt):
    _x = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _v = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _v_1 = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _x[0] = 1
    _v[0] = 0
    _v_1[0] = 0
    for i in range(int(_t / _dt)):
        f = -2 * _beta * _v[i] - _omega0 ** 2 * _x[i]
        _v_1[i + 1] = _v[i] + f * _dt
        f1 = -2 * _beta * _v_1[i + 1] - _omega0 ** 2 * _x[i]
        _v[i + 1] = 0.5 * (_v[i] + _v_1[i + 1] + f1 * _dt)
        _x[i + 1] = _x[i] + _v[i] * _dt
    return _x, _v


omega0 = 1
t = 100
dt = 0.5

beta = 0.1
x, v = damped_vibrations(beta, omega0, t, dt)
file = open('damper_vibration_1.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()

beta = 0.4
x, v = damped_vibrations(beta, omega0, t, dt)
file = open('damper_vibration_2.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()


# 受迫振动
def forced_oscillation(_beta, _omega0, _omega, _t, _dt):
    _x = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _v = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _v_1 = np.zeros(int(_t / _dt) + 1, dtype=np.float64)
    _x[0] = 1
    _v[0] = 0
    _v_1[0] = 0
    for i in range(int(_t / _dt)):
        f = -2 * _beta * _v[i] - _omega0 ** 2 * _x[i] + np.sin(_omega * i * _dt)
        _v_1[i + 1] = _v[i] + f * _dt
        f1 = -2 * _beta * _v_1[i + 1] - _omega0 ** 2 * _x[i] + np.sin(_omega * (i + 1) * _dt)
        _v[i + 1] = 0.5 * (_v[i] + _v_1[i + 1] + f1 * _dt)
        _x[i + 1] = _x[i] + _v[i] * _dt
    return _x, _v


omega = 0.5
x, v = forced_oscillation(beta, omega0, omega, t, dt)
file = open('forced_oscillation_1.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()

omega = 1
x, v = forced_oscillation(beta, omega0, omega, t, dt)
file = open('forced_oscillation_2.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()

omega = 2
x, v = forced_oscillation(beta, omega0, omega, t, dt)
file = open('forced_oscillation_3.txt', 'w')
for i in range(int(t / dt) + 1):
    file.write(str(i * dt) + ' ' + str(x[i]) + ' ' + str(v[i]) + '\n')
file.close()


# 画图
def plot(file_name, title):
    _file = open(file_name, 'r')
    _x, _y, _v = [], [], []
    for line in _file:
        _x.append(float(line.split()[0]))
        _y.append(float(line.split()[1]))
        _v.append(float(line.split()[2]))
    _file.close()
    plt.title(title)
    plt.plot(_x, _y, label='x')
    plt.plot(_x, _v, label='v')
    plt.legend()
    plt.savefig(file_name.split('.')[0] + '.png')
    plt.clf()


plot('damper_vibration_1.txt', 'Damper vibration 1')
plot('damper_vibration_2.txt', 'Damper vibration 2')
plot('forced_oscillation_1.txt', 'Forced oscillation 1')
plot('forced_oscillation_2.txt', 'Forced oscillation 2')
plot('forced_oscillation_3.txt', 'Forced oscillation 3')
