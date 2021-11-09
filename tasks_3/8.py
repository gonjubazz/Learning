a, b = list(map(lambda x: int(x), input().split(" ")))

for number in range(a, b + 1):
    result = ""
    for n in str(number):
        try:
            if number % int(n) == 0:
                result += n
                continue
        except ZeroDivisionError:
            result += "e"
        result += "e"

    if "e" not in result:
        print(number)
