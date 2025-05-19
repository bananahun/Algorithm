import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    res = 0
    while True:
        if lst[0] < max(lst):
            lst.append(lst.pop(0))
            if m > 0:
                m -= 1
            else:
                m = len(lst) - 1
        else:
            res += 1
            lst.pop(0)
            if m == 0:
                print(res)
                break
            else:
                m -= 1
