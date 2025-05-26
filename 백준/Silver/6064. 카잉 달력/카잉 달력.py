import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    k = x
    max_year = m * n
    while k <= max_year:
        if (k - y) % n == 0:
            print(k)
            break
        k += m
    else:
        print(-1)
