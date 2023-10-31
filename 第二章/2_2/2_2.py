import math

from matplotlib import pyplot as plt

v_t = open('v_t.txt', 'w')
a, v_0, t = 1 / 250, 10, 2000  # K/m，初速度，时间
v_1 = v_0  # 差商法
dt = 0.01
for i in range(int(t / dt)):
    tt = i * dt
    y = v_0 * math.exp(-a * tt)
    v_1 -= a * v_1 * dt
    v_t.write(str(tt) + ' ' + str(y) + ' ' + str(v_1) + '\n')
v_t.close()

x, y, y_1 = [], [], []
v_t = open('v_t.txt', 'r')
for line in v_t:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    y_1.append(float(line.split()[2]))
v_t.close()
plt.plot(x, y, label='v')
plt.plot(x, y_1, label='v_1')
plt.legend()
plt.savefig('2_2.png')
