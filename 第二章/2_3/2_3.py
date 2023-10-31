from matplotlib import pyplot as plt

A, B, x_0, v_0, t = -9.8, 0.5, 10, 0, 2
dt = 0.001
x, v = x_0, v_0
x_t = open('x_t.txt', 'w')
for i in range(int(t / dt)):
    x += v * dt
    v += (A - B * v) * dt
    x_t.write(str(i * dt) + ' ' + str(x) + '\n')
x_t.close()

x, y = [], []
x_t = open('x_t.txt', 'r')
for line in x_t:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
x_t.close()
plt.plot(x, y)
plt.savefig('2_3.png')
