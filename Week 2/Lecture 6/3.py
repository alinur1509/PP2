def multiply(l):
    f = 1
    for i in range(len(l)):
        f *= l[i]
    return f
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(multiply(nums))