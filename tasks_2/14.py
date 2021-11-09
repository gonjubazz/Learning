x, y = list(map(lambda x: float(x), input().split(" ")))

if (x < 0 and x ** 2 + y ** 2 < 2) or (0 <= x < y and x ** 2 + y ** 2 < 2):
    print("YES")
else:
    print("NO")