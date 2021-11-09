a, b = list(map(lambda x: int(x), input().split(" ")))

result = []
for i in range(a, b + 1):
    if str(i**2).endswith(str(i)):
        result.append(i)

if len(result) != 0:
    for i in result:
        print(i, end=' ')
else:
    print(-1)