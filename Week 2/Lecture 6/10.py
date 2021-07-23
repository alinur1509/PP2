def even(l):
    even = []
    for i in range(len(l)):
        l[i] = int(l[i])
        if l[i] % 2 == 0:
            even.append(l[i])
    return even
nums = input().split()
print(even(nums))   