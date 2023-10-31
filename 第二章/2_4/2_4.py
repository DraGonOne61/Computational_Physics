import math

from matplotlib import pyplot as plt

PI = 3.1415926

f1 = open('y1.txt', 'w')  # 入射波
f2 = open('y2.txt', 'w')  # 反射波
f_sum = open('y.txt', 'w')  # 合成波
# 振幅，频率，波长
A, T, l = 2, 3, 5
for i in range(1, 10001):
    t = i / 1000
    y1 = A * math.cos(2 * PI * (t / T - t / l))
    y2 = A * math.cos(2 * PI * (t / T + t / l))
    y = y1 + y2
    f1.write(str(t) + ' ' + str(y1) + '\n')
    f2.write(str(t) + ' ' + str(y2) + '\n')
    f_sum.write(str(t) + ' ' + str(y) + '\n')
f1.close()
f2.close()
f_sum.close()

x1, y1, x2, y2, x, y = [], [], [], [], [], []
f1 = open('y1.txt', 'r')
f2 = open('y2.txt', 'r')
f_sum = open('y.txt', 'r')
for line in f1:
    x1.append(float(line.split()[0]))
    y1.append(float(line.split()[1]))
for line in f2:
    x2.append(float(line.split()[0]))
    y2.append(float(line.split()[1]))
for line in f_sum:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
f1.close()
f2.close()
f_sum.close()
plt.plot(x1, y1, label='y1')
plt.plot(x2, y2, label='y2')
plt.plot(x, y, label='y')
plt.legend()
plt.savefig('2_4.png')
