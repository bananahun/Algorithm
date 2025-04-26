import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def bfs(x, y, lst, visited, a, b):
    dq = deque()
    dq.append((x, y))
    visited[y][x] = True
    
    while dq:
        cx, cy = dq.popleft()
        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < a and 0 <= ny < b:
                if lst[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((nx, ny))

def search():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        lst = [list(map(int, input().split())) for _ in range(b)]
        visited = [[False] * a for _ in range(b)]
        cnt = 0
        for y in range(b):
            for x in range(a):
                if lst[y][x] == 1 and not visited[y][x]:
                    bfs(x, y, lst, visited, a, b)
                    cnt += 1
        print(cnt)

search()
