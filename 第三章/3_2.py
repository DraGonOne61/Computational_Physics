# 对圆盘轴线上一点电场强度E的大小可表示为：
# E=σx/2ε0 ∫^R2_R1 r*dr/((x^2+r^2)^(3/2))
# 用解析法和三种基本数值方法计算E，分别取
# 1.R1=0.01m,R2=1m
# 2.R1=0.01m,R2=10m
# 其中σ=0.5，x=0.01m

from numpy import sqrt
from scipy.constants import epsilon_0


def f(r):
    return sigma * r / (2 * epsilon_0 * sqrt(x ** 2 + r ** 2))


# 解析法
def analytic(_x, _r1, _r2):
    return sigma / (2 * epsilon_0) * (sqrt(_x ** 2 + _r2 ** 2) - sqrt(_x ** 2 + _r1 ** 2))


# 矩形法
def rectangle(_r1, _r2, _f, _n):
    y = 0
    for i in range(1, _n):
        x = _r1
        x += i * (_r2 - _r1) / _n
        y += _f(x) * (_r2 - _r1) / _n
    return y


# 梯形法
def trapezoidal(_r1, _r2, _f, _n):
    y = 0
    for i in range(0, _n + 1):
        x = _r1
        x += i * (_r2 - _r1) / _n
        if i == 0 or i == _n:
            y += 0.5 * _f(x) * (_r2 - _r1) / _n
        else:
            y += _f(x) * (_r2 - _r1) / _n
    return y


# 辛普森法
def simpson(_r1, _r2, _f, _n):
    y = 0
    for i in range(0, _n + 1):
        x = _r1
        x += i * (_r2 - _r1) / _n
        if i == 0 or i == _n:
            y += 1 / 3 * _f(x) * (_r2 - _r1) / _n
        else:
            k = i - 2 * (i // 2)
            if k == 0:
                y += 2 / 3 * _f(x) * (_r2 - _r1) / _n
            else:
                y += 4 / 3 * _f(x) * (_r2 - _r1) / _n
    return y


sigma = 0.5
n = 1000
x = 0.01
r1 = 0.01
r2 = 1
print("(1)")
print(f'解析法：E = {analytic(x, r1, r2):.4f}')
print(f'矩形法：E = {rectangle(r1, r2, f, n):.4f}')
print(f'梯形法：E = {trapezoidal(r1, r2, f, n):.4f}')
print(f'辛普森法：E = {simpson(r1, r2, f, n):.4f}')

r2 = 10
print("(2)")
print(f'解析法：E = {analytic(x, r1, r2):.4f}')
print(f'矩形法：E = {rectangle(r1, r2, f, n):.4f}')
print(f'梯形法：E = {trapezoidal(r1, r2, f, n):.4f}')
print(f'辛普森法：E = {simpson(r1, r2, f, n):.4f}')
