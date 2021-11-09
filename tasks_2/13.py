x, y = list(map(lambda x: float(x), input().split(" ")))

if x ** 2 - 2 < y < -x or x ** 2 - 2 < y < x:
    print("YES")
else:
    print("NO")
