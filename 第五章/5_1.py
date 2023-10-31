# 用高斯列主元消去法求解线性方程组
# -x1+2*x2-2*x3=-1
# 3*x1-x2+4*x3=7
# 2*x1-3*x2-2*x3=0

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


n = 3
a = np.array([[-1, 2, -2], [3, -1, 4], [2, -3, -2]])
b = np.array([-1, 7, 0])
x = guass(n, a, b)
print(x)
