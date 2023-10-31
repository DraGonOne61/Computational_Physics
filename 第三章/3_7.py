# 用变步长辛普森法计算积分
# G=∫^1_0arctan(x)/x dx
# 此积分值称为Catalan常数，G的真值为0.915965。要求误差不超过1e-5

from numpy import arctan


def f(x):
    if x == 0:
        return 1
    else:
        return arctan(x) / x


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


ep = 1e-5
s2 = [0]
print(f'G = {simpson_step(0, 1, ep, s2, f):.6f}')
