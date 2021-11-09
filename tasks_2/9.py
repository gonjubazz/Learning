
p = list(map(lambda x: float(x), input().split(" ")))

result = ""
if p[1] < 1:
    result += "1"
else:
    result += "0"

if p[1] < -p[0]:
    result += "1"
else:
    result += "0"

if p[0]**2 + p[1]**2 < 1:
    result += "1"
else:
    result += "0"

if (p[0]-1)**2 + p[1]**2 < 1:
    result += "1"
else:
    result += "0"

print(result)
