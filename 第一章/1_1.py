n = 1
T = 0
while True:
    T += n ** 3
    if T > 10 ** 4:
        print(f'N = {n}, T = {T}')
        break
    n += 1
