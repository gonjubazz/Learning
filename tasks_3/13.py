n = input()

last = ""
found = False
for i in n:
    if i == last:
        found = True
    last = i

if found:
    print("YES")
else:
    print("NO")
