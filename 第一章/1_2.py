x = float(input())
y = 0
if 0 <= x < 10:
    y = x
elif 10 <= x < 20:
    y = x ** 2 + 1
elif 20 <= x < 30:
    y = x ** 3 + x ** 2 + 1

print(y)
