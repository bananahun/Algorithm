'''
0 - safe
1 - war
2 - virus
---
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27
---
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9
---
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3
'''
import sys
import copy
from collections import deque
from itertools import combinations

# print(list(combinations([1,2,3,4,5],3)))

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def countt(check_lst):
    dq = deque()
    for i in range(n):
        for j in range(m):
            if check_lst[i][j] == 2:
                dq.append((i, j))

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check_lst[nx][ny] == 0:
                    check_lst[nx][ny] = 2
                    dq.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if check_lst[i][j] == 0:
                cnt += 1
    return cnt


war = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            war.append([i, j])

max_cnt = 0
for walls in combinations(war, 3):
    for x, y in walls:
        lst[x][y] = 1

    check_lst = copy.deepcopy(lst)
    result = countt(check_lst)
    if result > max_cnt:
        max_cnt = result

    for x, y in walls:
        lst[x][y] = 0

print(max_cnt)
