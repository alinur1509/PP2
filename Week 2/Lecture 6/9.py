def isPrime(n):
    cnt = 0
    for i in range(2, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 1:
        return 'The input number is prime'
    else:
        return 'The input number is not prime'
n = int(input())
if n < 2:
    print('Please choose positive number, that is higher than 2.')
else:
    print(isPrime(n))