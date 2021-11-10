n = input()

i = 0
result = False
for a in n:

    try:
        if n[i-1] == a == n[i+1]:
            result = True
        else:
            result = False
    except IndexError:
        pass
    i += 1

if result is True:
    print("YES")
else:
    print("NO")

