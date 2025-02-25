import sys
from collections import deque
input = sys.stdin.readline

'''
6 5 -> 정점 갯수, 간선 갯수
1 2
2 5
5 1
3 4
4 6
'''
n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)


def dfs(num):
    global count
    visited[num] = True
    for i in lst[num]:
        if not visited[i]:
            dfs(i)

for j in range(1, n+1):
    if visited[j] == False:
        dfs(j)
        count += 1
        
print(count)