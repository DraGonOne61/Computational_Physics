i_0 = 0.18232156
i_21 = 0
i = i_0
for n in range(1, 21):
    temp = i
    i = -5 * temp + 1 / n
    print(f'i_{n} = {i}')

print('------------------')

i = i_21
for n in range(21, 1, -1):
    temp = i
    i = -1 / 5 * temp + 1 / (5 * n)
    print(f'i_{n - 1} = {i}')
