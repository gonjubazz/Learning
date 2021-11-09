a, b = list(map(lambda x: int(x), input().split(" ")))

result = []
for a in range(a, b + 1):
    a_str = str(a)
    lng = len(a_str)
    summ = 0
    for i in a_str:
        summ += int(i) ** lng

    if summ == a:
        result.append(a)

if len(result) != 0:
    for i in result:
        print(i, end=' ')
else:
    print(-1)