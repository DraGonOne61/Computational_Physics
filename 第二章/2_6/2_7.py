import numpy as np
import plotly
from matplotlib import pyplot as plt

f = open('data.txt', 'w')
point1 = [30, 50]
point2 = [70, 50]
lamda = 6
for i in range(100):
    distance = []
    for j in range(100):
        point = [j, i]
        x = np.sqrt((point[0] - point1[0]) ** 2 + (point[1] - point1[1]) ** 2) % lamda / lamda
        y = np.sqrt((point[0] - point2[0]) ** 2 + (point[1] - point2[1]) ** 2) % lamda / lamda
        xx = np.sin(x * 2 * np.pi)
        yy = np.sin(y * 2 * np.pi)
        distance.append(xx + yy)
    f.write(str(distance)[1:-1] + "\n")
f.close()

# 三维图
z = []
f = open('data.txt', 'r')
for line in f:
    data = []
    for i in line.split(','):
        data.append(float(i))
    z.append(data)
f.close()
matrix = [[20 for zij in zi] for zi in z]
plotly.offline.plot([
    dict(
        z=z,
        type="surface"
    ),
    dict(
        z=matrix,
        showscale=False,
        opacity=0.01,  # 透明度
        type="surface"
    )
], filename="pic.html")

# 二维图
x, y, z = [], [], []
f = open('data.txt', 'r')
for line in f:
    data = []
    for i in line.split(','):
        data.append(float(i))
    z.append(data)
f.close()
for i in range(100):
    x.append(i)
    y.append(i)
plt.contourf(x, y, z, 8, alpha=0.75, cmap=plt.cm.hot)
plt.savefig('pic.png')
