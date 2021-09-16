import random

_input = input().split(" ")

for i in range(5):
    result = random.uniform(float(_input[0]), float(_input[1]))
    print(float('{:.3f}'.format(result)))
