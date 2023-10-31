v_0 = 20
k = 1 / 300
t = 15
# 步长
dt = 0.01
v = v_0
s = 0
for i in range(int(t / dt)):
    v -= k * v ** 2 * dt
    s += v * dt
print(f'15秒后快艇的速率为 {v} m/s，所走的路程为 {s} m')
