x, y = list(map(lambda x: float(x), input().split(" ")))

if x < 2 and y < x and x * x + y * y > 4:
    print("YES")
else:
    print("NO")
