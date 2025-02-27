import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]
    building = []
    dq = deque()

    for z in range(l):
        lst = [list(input().rstrip()) for _ in range(r)]
        building.append(lst)
        input()
        for y in range(r):
            for x in range(c):
                if lst[y][x] == 'S':
                    start = (z, y, x)
                    dq.append(start)
                    visited[z][y][x] = 0

    check = False
    while dq:
        nz, ny, nx = dq.popleft()

        if building[nz][ny][nx] == 'E':
            print(f"Escaped in {visited[nz][ny][nx]} minute(s).")
            check = True
            break
        
        for i in range(6):
            cz, cy, cx = nz + dz[i], ny + dy[i], nx + dx[i]
            if 0 <= cz < l and 0 <= cy < r and 0 <= cx < c:
                if visited[cz][cy][cx] == -1 and building[cz][cy][cx] != '#':
                    visited[cz][cy][cx] = visited[nz][ny][nx] + 1
                    dq.append((cz, cy, cx))

    if not check:
        print("Trapped!")
