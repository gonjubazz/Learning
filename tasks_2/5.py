data = input().split(" ")

count = 0

for n in data:
    index = data.index(n)
    try:
        if n == data[index - 1] or n == data[index + 1]:
            count += 1
    except IndexError:
        break

print(count)
