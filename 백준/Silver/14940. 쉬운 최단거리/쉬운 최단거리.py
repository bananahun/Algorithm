import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    dq = deque([[x, y]])
    visited[y][x] = 0  # 목표 지점에서 시작 (0부터 거리 측정)

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                dq.append([nx, ny])

sx, sy = -1, -1
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            sx, sy = j, i
        elif lst[i][j] == 1:
            visited[i][j] = -1

bfs(sx, sy)

for row in visited:
    print(*row)
