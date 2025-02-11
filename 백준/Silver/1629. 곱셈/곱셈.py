import sys
input = sys.stdin.readline

def fun(a, b, c):
    if (b == 1):
        return a % c

    X = fun(a, b//2, c)

    if (b % 2 == 0):
        return X * X % c
    else:
        return a * X * X % c

a, b, c = map(int, input().split())

print(fun(a, b, c))
