# 用龙贝格法计算积分
# I=∫^0.6_0.1 0.02792*(2-x)/((1.449*x+1)^0.8*(1-x)^1.2*x) dx
# 要求误差不超过1e-5


def f(x):
    return 0.02792 * (2 - x) / ((1.449 * x + 1) ** 0.8 * (1 - x) ** 1.2 * x)


def romberg(_a, _b, _ep, _f):
    h = _b - _a
    t1 = h / 2 * (_f(_a) + _f(_b))
    n = 1
    s1 = 0
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0
    while True:
        s = 0
        for i in range(1, n + 1):
            s += _f(_a + (i - 0.5) * h)
        t2 = (t1 + h * s) / 2
        s2 = (4 * t2 - t1) / 3
        if n != 1:
            c2 = s2 + (s2 - s1) / 15
            if n != 2:
                r2 = c2 + (c2 - c1) / 63
                if n != 4:
                    if abs(r2) < 1:
                        if abs(r2 - r1) < _ep:
                            return r2
                    else:
                        if abs((r2 - r1) / r2) < _ep:
                            return r2
                r1 = r2
            c1 = c2
        s1 = s2
        t1 = t2
        h /= 2
        n *= 2


ep = 1e-5
print(f'I = {romberg(0.1, 0.6, ep, f):.6f}')
