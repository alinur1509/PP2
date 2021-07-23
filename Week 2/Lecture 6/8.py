def unique_list(l):
    unique = []
    for i in l:
        if i not in unique:
            unique.append(i)
        else:
            continue
    return unique
l = input().split()
print(unique_list(l))