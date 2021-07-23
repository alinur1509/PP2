def count_case(s):
    cntl = 0
    cntu = 0
    for i in s:
        if i.isupper():
            cntu += 1
        if i.islower():
            cntl += 1
    return cntu, cntl
s = input()
print(f'No. of Upper case characters: {count_case(s)[0]}\nNo. of Lower case Characters: {count_case(s)[1]}')