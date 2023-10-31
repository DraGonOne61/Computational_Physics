# 结合理想气体平衡状态下的麦克斯韦速率分布律，用辛普森法计算0℃下氮气、
# 氧气分子运动的平均速率v和方均根速率v_rms，并于解析解v=1.59*sqr(RT/M)
# v_rms=1.73*sqr(RT/M)比较，其中M是气体的摩尔质量，R=8.31，为摩尔气体常数。

from numpy import pi, exp, sqrt
from scipy.constants import Avogadro as Av
from scipy.constants import Boltzmann as Kb


def f(_v):
    return 4 * pi * (_v ** 2) * (m / (2 * pi * Kb * T)) ** (3 / 2) * exp(-m * _v ** 2 / (2 * Kb * T))


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


R = 8.31
T = 273.15
M = 32e-3  # 氧气
# M = 28e-3  # 氮气
m = M / Av
n = 1000
a = 0
b = 1000
print(f'v = {simpson(a, b, lambda v: v * f(v), n):.4f}')
print(f'v_rms = {sqrt(simpson(a, b, lambda v: v ** 2 * f(v), n)):.4f}')
print(f'v = {1.59 * sqrt(R * T / M):.4f}')
print(f'v_rms = {1.73 * sqrt(R * T / M):.4f}')
