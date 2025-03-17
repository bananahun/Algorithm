import math

def check(n):
    return int(math.sqrt(n)) ** 2 == n

def check_four(n):
    if check(n):
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if check(n - i * i):
            return 2

    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4

    return 3

n = int(input())
print(check_four(n))
