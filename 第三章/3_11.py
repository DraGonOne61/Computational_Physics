# 用n=2，4的高斯求积公式计算积分
# G=∫^π/2_0 dx/(cos^2(x)+4sin^2(x)) = π/4

from numpy import cos, sin, pi


def f(x):
    return 1 / (cos(x) ** 2 + 4 * sin(x) ** 2)


def gauss_2(_a, _b, _f):
    t = [-0.57735, 0.57735]
    w = [1, 1]
    G = 0
    for i in range(2):
        G += w[i] * _f((_b - _a) / 2 * t[i] + (_a + _b) / 2)
    return G * (_b - _a) / 2


def gauss_4(_a, _b, _f):
    t = [0.339981, -0.339981, 0.861136, -0.861136]
    w = [0.652145, 0.652145, 0.347855, 0.347855]
    G = 0
    for i in range(4):
        G += w[i] * _f((_b - _a) / 2 * t[i] + (_a + _b) / 2)
    return G * (_b - _a) / 2


print(f'G = {gauss_2(0, pi / 2, f):.6f}')
print(f'G = {gauss_4(0, pi / 2, f):.6f}')
