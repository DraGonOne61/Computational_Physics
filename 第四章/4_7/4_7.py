# 用龙格库塔法求初值问题
# y'‘+2*t*y'+t^2*y=e^t (0<=t<=1)
# y(0)=1, y'(0)=-1
# 步长h=0.1

import numpy as np
from matplotlib import pyplot as plt


def f(_t, _y, _v):
    return _v


def g(_t, _y, _v):
    return np.exp(_t) - 2 * _t * _v - _t ** 2 * _y


def runge_kutta(_t, _y, _v, _h):
    k1 = f(_t, _y, _v)
    l1 = g(_t, _y, _v)
    k2 = f(_t + _h / 2, _y + _h / 2 * k1, _v + _h / 2 * l1)
    l2 = g(_t + _h / 2, _y + _h / 2 * k1, _v + _h / 2 * l1)
    k3 = f(_t + _h / 2, _y + _h / 2 * k2, _v + _h / 2 * l2)
    l3 = g(_t + _h / 2, _y + _h / 2 * k2, _v + _h / 2 * l2)
    k4 = f(_t + _h, _y + _h * k3, _v + _h * l3)
    l4 = g(_t + _h, _y + _h * k3, _v + _h * l3)
    _y += _h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    _v += _h / 6 * (l1 + 2 * l2 + 2 * l3 + l4)
    return _y, _v


t = 0
y = 1
v = -1 # y'
h = 0.1
t_list = []
y_list = []
v_list = []
t_list.append(t)
y_list.append(y)
v_list.append(v)
while t <= 1:
    y, v = runge_kutta(t, y, v, h)
    t += h
    t_list.append(t)
    y_list.append(y)
    v_list.append(v)
file = open('runge_kutta.txt', 'w')
for i in range(len(t_list)):
    file.write(str(t_list[i]) + ' ' + str(y_list[i]) + ' ' + str(v_list[i]) + '\n')
file.close()

# 画图
file = open('runge_kutta.txt', 'r')
x, y, v = [], [], []
for line in file:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    v.append(float(line.split()[2]))
file.close()
plt.title('runge kutta')
plt.plot(x, y, label='y')
plt.plot(x, v, label='v')
plt.legend()
plt.savefig('runge_kutta.png')

