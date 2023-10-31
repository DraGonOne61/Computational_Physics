# 用4点高斯求积公式计算积分
# I=∫^2_1.4 ∫^1.5_1 ln(x+y) dx dy

from numpy import log

def f(x, y):
    return log(x + y)


def gauss_4(_a, _b, _c, _d, _f):
    t = [0.339981, -0.339981, 0.861136, -0.861136]
    w = [0.652145, 0.652145, 0.347855, 0.347855]
    G = 0
    for i in range(4):
        for j in range(4):
            G += w[i] * w[j] * _f((_b - _a) / 2 * t[i] + (_a + _b) / 2, (_d - _c) / 2 * t[j] + (_c + _d) / 2)
    return G * (_b - _a) * (_d - _c) / 4


print(f'I = {gauss_4(1, 1.5, 1.4, 2, f):.6f}')
