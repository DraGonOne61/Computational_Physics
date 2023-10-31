# 某一装置运动轨迹为一圆锥曲线
# x^2+b*x*y+c*y^2+d*x+e*y+f=0
# 在运动轨迹上测得5个点的坐标：
# c1(14.38, 3.94), c2(11.38, 2.79), c3(7.42, 3.07), c4(6.38, 5.11), c5(8.81, 2.59)
# 形成b, c, d, e, f所满足得方程，用列主元消去法求解b, c, d, e, f的近似值


import numpy as np


def guass(_n, _a, _b):
    for k in range(_n - 1):
        p = 0  # 最大主元
        i0 = 0  # 最大主元所在行
        for i in range(k, _n):
            if abs(_a[i][k]) > abs(p):
                p = _a[i][k]
                i0 = i
        for j in range(k, _n):  # 交换第k行与最大主元所在行
            t = _a[k][j]
            _a[k][j] = _a[i0][j]
            _a[i0][j] = t
        t = _b[k]
        _b[k] = _b[i0]
        _b[i0] = t
        for i in range(k + 1, _n):
            m = _a[i][k] / _a[k][k]  # 消去系数
            for j in range(k, _n):
                _a[i][j] -= m * _a[k][j]
            _b[i] -= m * _b[k]
    _x = np.zeros(_n).reshape(_n, 1)
    _x[_n - 1] = _b[_n - 1] / _a[_n - 1][_n - 1]  # 回代
    for i in range(_n - 2, -1, -1):
        s = 0
        for j in range(i + 1, _n):
            s += _a[i][j] * _x[j]
        _x[i] = (_b[i] - s) / _a[i][i]
    return _x


n = 5
a = np.array([[14.38 * 3.94, 3.94 ** 2, 14.38, 3.94, 1],
              [11.38 * 2.79, 2.79 ** 2, 11.38, 2.79, 1],
              [7.42 * 3.07, 3.07 ** 2, 7.42, 3.07, 1],
              [6.38 * 5.11, 5.11 ** 2, 6.38, 5.11, 1],
              [8.81 * 2.59, 2.59 ** 2, 8.81, 2.59, 1]])
b = np.array([-14.38 ** 2, -11.38 ** 2, -7.42 ** 2, -6.38 ** 2, -8.81 ** 2])
x = guass(n, a, b)
print(x)
