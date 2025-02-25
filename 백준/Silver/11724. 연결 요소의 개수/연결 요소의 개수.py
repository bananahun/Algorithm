import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(num):
    stack = [num]  # 스택에 시작 노드를 넣어줍니다.
    visited[num] = True
    
    while stack:
        node = stack.pop()  # 스택에서 하나씩 꺼냄
        for i in lst[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
