import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        a, b = input().split()
        if b in dict:
            dict[b] += 1
        else:
            dict[b] = 1

    result = 1
    for i in dict.values():
        result *= (i + 1)

    print(result - 1)