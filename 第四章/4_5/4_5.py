# 用二级欧拉近似法和龙格库塔法计算
# y'=1+e^(-t)*sin(y) (0<=t<=1)
# y(0)=0
# 步长h=0.1


import numpy as np
from matplotlib import pyplot as plt


def f(_t, _y):
    return 1 + np.exp(-_t) * np.sin(_y)


def euler_2(_t, _y, _h):
    _y += _h * f(_t, _y)
    _y += _h * f(_t + _h, _y)
    return _y


def runge_kutta(_t, _y, _h):
    k1 = f(_t, _y)
    k2 = f(_t + _h / 2, _y + _h / 2 * k1)
    k3 = f(_t + _h / 2, _y + _h / 2 * k2)
    k4 = f(_t + _h, _y + _h * k3)
    _y += _h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return _y


t = 0
y = 0
h = 0.1
t_list = []
y_list = []
t_list.append(t)
y_list.append(y)
while t <= 1:
    y = runge_kutta(t, y, h)
    t += h
    t_list.append(t)
    y_list.append(y)
file = open('runge_kutta.txt', 'w')
for i in range(len(t_list)):
    file.write(str(t_list[i]) + ' ' + str(y_list[i]) + '\n')
file.close()

t = 0
y = 0
h = 0.1
t_list = []
y_list = []
t_list.append(t)
y_list.append(y)
while t <= 1:
    y = euler_2(t, y, h)
    t += h
    t_list.append(t)
    y_list.append(y)
file = open('euler_2.txt', 'w')
for i in range(len(t_list)):
    file.write(str(t_list[i]) + ' ' + str(y_list[i]) + '\n')
file.close()


def plot(file_name, title):
    _file = open(file_name, 'r')
    _x, _y = [], []
    for line in _file:
        _x.append(float(line.split()[0]))
        _y.append(float(line.split()[1]))
    _file.close()
    plt.title(title)
    plt.plot(_x, _y)
    plt.savefig(file_name.split('.')[0] + '.png')
    plt.clf()


plot('runge_kutta.txt', 'runge_kutta')
plot('euler_2.txt', 'euler_2')

