def check(n, a, b):
    if a <= n <= b:
        return 'The input number is in range'
    else:
        return 'The input number is not in range'
n, a, b = int(input('Input number: ')), int(input('Start of range: ')), int(input('End of range: '))
print(check(n, a, b))