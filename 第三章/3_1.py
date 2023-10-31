# 分别用矩形法、梯形法、抛物线法求积分（N=1000）
# # ∫^π_0 cos(1/(1+x^2))dx

from numpy import pi, cos


def f(x):
    return cos(1 / (1 + x ** 2))


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


r1 = 0
r2 = pi
n = 1000
print(f'矩形法：{rectangle(r1, r2, f, n)}')
print(f'梯形法：{trapezoidal(r1, r2, f, n)}')
print(f'抛物线法：{simpson(r1, r2, f, n)}')
