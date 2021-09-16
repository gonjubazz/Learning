import math

p = input().split(" ")
p2 = input().split(" ")

distance = math.sqrt(
    (float(p2[0]) - float(p[0])) ** 2 +
    (float(p2[1]) - float(p[1])) ** 2)

print(float('{:.3f}'.format(distance)))