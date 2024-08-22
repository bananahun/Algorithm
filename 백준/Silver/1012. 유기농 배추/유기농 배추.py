from collections import deque;

def bfs(x,y):           
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dq = deque()
    dq = [(x,y)]
    arr[x][y] = 0 # 방문처리
    while dq:
        x,y = dq.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 1 :
                dq.append((nx,ny))
                arr[nx][ny] = 0

T = int(input())
for i in range(T):
    M, N, K = map(int,input().split())
    arr = [[0]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x,y = map(int, input().split())
        arr[x][y] = 1

    for a in range(M):
        for b in range(N):
            if arr[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)
                

    