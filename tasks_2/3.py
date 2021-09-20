data = input().split(" ")

dc = {
    "A": int(data[0]),
    "B": int(data[1]),
    "C": int(data[2])
}

_max = max(dc)
_min = min(dc)

print(_max, _min)
