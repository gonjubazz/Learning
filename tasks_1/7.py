import random

_input = input().split(" ")

for i in range(5):
    print(random.randint(int(_input[0]), int(_input[1])))