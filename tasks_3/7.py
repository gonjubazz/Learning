a, b = list(map(lambda x: int(x), input().split(" ")))
c, d = list(map(lambda x: int(x), input().split(" ")))

result = []
for i in range(10000, 99999):
        if i % a == b and i % c == d:
            result.append(i)

if len(result) != 0:
    for i in result:
        print(i, end=' ')
else:
    print(-1)
