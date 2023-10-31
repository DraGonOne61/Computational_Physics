# 用3点及5点高斯求积公式计算积分∫^3_1 1/x dx，并于梯形法、辛普森法作比较


def f(x):
    if x == 0:
        return 1
    else:
        return 1 / x


def gauss_3(_a, _b, _f):
    t = [0, 0.774597, -0.774597]
    w = [0.888889, 0.555556, 0.555556]
    G = 0
    for i in range(3):
        G += w[i] * _f((_b - _a) / 2 * t[i] + (_a + _b) / 2)
    return G * (_b - _a) / 2


def gauss_5(_a, _b, _f):
    t = [0, 0.90618, -0.90618, 0.538469, -0.538469]
    w = [0.568889, 0.478629, 0.478629, 0.236927, 0.236927]
    G = 0
    for i in range(5):
        G += w[i] * _f((_b - _a) / 2 * t[i] + (_a + _b) / 2)
    return G * (_b - _a) / 2


# 矩形法
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


a = 1
b = 3
n = 1000
print(f'3点高斯求积公式：{gauss_3(a, b, f):.4f}')
print(f'5点高斯求积公式：{gauss_5(a, b, f):.4f}')
print(f'矩形法：{trapezoidal(a, b, f, n):.4f}')
print(f'辛普森法：{simpson(a, b, f, n):.4f}')
