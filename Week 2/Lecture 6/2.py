def sumoflist(l):
    return sum(l)
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(sumoflist(nums))