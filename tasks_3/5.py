data = input().split(" ")

result = 0
for i in range(int(data[0]), int(data[1])+1):
    result += i*i

print(result)