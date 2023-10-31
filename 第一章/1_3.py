n = 1
s = 1
while True:
    p = 1 / (n * (n + 1))
    s += p
    if p < 10 ** -3:
        print(f'N = {n}, S = {s}, P = {p}')
        break
    n += 1
