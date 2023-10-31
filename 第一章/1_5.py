e = 1e-3
t = 0
while True:
    delta_a = 6 * t ** 3 - 1
    if abs(delta_a) < 1e-2:
        print(f't = {t}')
        break
    t += e
