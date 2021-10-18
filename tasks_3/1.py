import math

data = input().split(" ")

result = 0
for i in range(int(math.fabs(int(data[1])))):
    if int(data[1]) > 0:
        result += int(data[0])
    elif int(data[1]) < 0:
        result -= int(data[0])
    else:
        print("0")
print(result)