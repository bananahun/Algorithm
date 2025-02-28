import sys
from collections import deque

input = sys.stdin.readline

def bfs(s, e):
    dq = deque([s])
    visited[s] = 0
    while dq:
        x = dq.popleft()
        if x == e:
            return
        for nx in [2*x, x-1, x+1]:
            if 0 <= nx < 10**6 and visited[nx] == -1:
                if nx == 2*x:
                    visited[nx] = visited[x]
                    dq.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    dq.append(nx)

s, e = map(int, input().split())
visited = [-1] * (10**6)
bfs(s, e)
print(visited[e])
