x, y = list(map(lambda x: float(x), input().split(" ")))

if (2 - x ** 2 > y > x and x < 0) | (2 - x ** 2 > y > x >= 0):
    print("YES")
else:
    print("NO")
