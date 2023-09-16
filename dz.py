a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if d > 0:
    print(((-b + d ** 0.5) / 2 * a), ((-b - d ** 0.5) / 2 * a))
if d == 0:
    print(-b / 2 * a)
if d < 0:
    print("Нет корней!")