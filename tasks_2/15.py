x, y = list(map(lambda x: float(x), input().split(" ")))

if -x < y < x and x ** 2 + y ** 2 < 2:
    print("YES")
else:
    print("NO")