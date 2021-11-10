count = int(input())
nums = []
for i in range(count):
    nums.append(int(input()))

res_1 = 0
res_2 = nums[0]
for n in nums:
    res_1 += n
    try:
        res_2 *= nums[nums.index(n)+1]
    except IndexError:
        pass

print(res_1, res_2)