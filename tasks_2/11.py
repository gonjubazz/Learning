from math import sin

x, y = list(map(lambda x: float(x), input().split(" ")))

if 0.5 >= y >= 0 and y <= sin(x) and 0 < x < 3.1415:
    print("YES")
else:
    print("NO")
