n = input().split(" ")
n[0]=int(n[0])
n[1]=int(n[1])
n[2]=int(n[2])

result_1 = n[0] + n[1] + n[2]
result_2 = n[0] * n[1] * n[2]
result_3 = (n[0] + n[1] + n[2]) / 3

print(f"{n[0]}+{n[1]}+{n[2]}={result_1}")
print(f"{n[0]}*{n[1]}*{n[2]}={result_2}")
print(f"({n[0]}+{n[1]}+{n[2]})/3=" + '{:.3f}'.format(result_3))