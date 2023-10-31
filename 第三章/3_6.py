# 椭圆方程为x^2/a^2+y^2/b^2=1，则椭圆周长的计算公式为
# L=∫^π_0 sqrt(a^2sin^2(x)+b^2cos^2(x))dx
# 用辛普森法和变步长辛普森法计算椭圆x^2/400+y^2/100=1的周长

from numpy import sin, cos, pi, sqrt


def f(x):
    return sqrt(a ** 2 * sin(x) ** 2 + b ** 2 * cos(x) ** 2)


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


# 变步长辛普森法
def simpson_step(_a, _b, _ep, _s2, _f):
    d = 0
    h = _b - _a
    t1 = h / 2 * (_f(_a) + _f(_b))
    n = 1
    s1 = 0
    while True:
        s = 0
        for i in range(1, n + 1):
            s += _f(_a + (i - 0.5) * h)
        t2 = (t1 + h * s) / 2
        _s2[0] = t2 + (t2 - t1) / 3
        if n != 1:
            if abs(_s2[0]) <= 1:
                d = abs(_s2[0] - s1)
            elif abs(_s2[0]) > 1:
                d = abs((_s2[0] - s1) / _s2[0])
            if d < _ep:
                break
        s1 = _s2[0]
        t1 = t2
        h /= 2
        n *= 2
    return _s2[0]


a = 20
b = 10
ep = 1e-5
s2 = [0]
print(f'L = {simpson(0, pi, f, 1000):.4f}')
print(f'L = {simpson_step(0, pi, ep, s2, f):.4f}')
