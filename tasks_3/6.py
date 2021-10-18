import random

data = input().split(" ")

result = ""
for i in range(int(data[2])):
    result += f"{random.randint(int(data[0]), int(data[1]))} "

print(result)