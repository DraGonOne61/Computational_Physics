import math

from matplotlib import pyplot as plt

PI = 3.1415926

f1 = open('x1.txt', 'w')
f2 = open('x2.txt', 'w')
f_sum = open('x.txt', 'w')
A1, A2, w_PI, phi1_PI, phi2_PI = map(float, input().split())  # 振幅，角频率，相位
for i in range(1, 201):
    t = i / 1000
    x1 = A1 * math.cos(w_PI * PI * t + phi1_PI * PI)
    x2 = A2 * math.cos(w_PI * PI * t + phi2_PI * PI)
    x = x1 + x2
    f1.write(str(t) + ' ' + str(x1) + '\n')
    f2.write(str(t) + ' ' + str(x2) + '\n')
    f_sum.write(str(t) + ' ' + str(x) + '\n')
f1.close()
f2.close()
f_sum.close()

x1, y1, x2, y2, x, y = [], [], [], [], [], []
f1 = open('x1.txt', 'r')
f2 = open('x2.txt', 'r')
f_sum = open('x.txt', 'r')
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
plt.plot(x1, y1, label='x1')
plt.plot(x2, y2, label='x2')
plt.plot(x, y, label='x')
plt.legend()
plt.savefig('2_1.png')
