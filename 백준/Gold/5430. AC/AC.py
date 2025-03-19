import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    fun = input().strip()
    N = int(input())
    str_input = input().strip()

    if N == 0:
        lst = deque()
    else:
        lst = deque(map(int, str_input[1:-1].split(",")))

    check = True

    for i in fun:
        if i == 'R':
            check = not check
        else:
            if not lst:
                print('error')
                break
            if check:
                lst.popleft()
            else:
                lst.pop()
    else:
        if not check:
            lst.reverse()
        print(f"[{','.join(map(str, lst))}]")
