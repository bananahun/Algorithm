import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
rain = max(map(max, lst))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    global cnt
    q = deque()
    q.append((i,j))
    sink[i][j] = True
    cnt += 1 
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if nx<0 or ny < 0 or nx >= N or ny >= N:
                continue
            if sink[nx][ny]==False: 
                sink[nx][ny] = True 
                q.append((nx,ny))
count_list = []
for rain in range(rain): 
    cnt = 0 
    sink = [[False for _ in range(N)] for i in range(N)] 
    for i in range(N):
        for j in range(N):
            if lst[i][j]<=rain:
                sink[i][j]=True 
    for i in range(N):
        for j in range(N):
            if sink[i][j]==False: 
                bfs(i,j) 
    count_list.append(cnt)  

print(max(count_list))