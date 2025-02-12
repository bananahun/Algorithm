import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []
visited = [False] * (n+1)

def f():
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            res.append(i)
            f()
            res.pop()
            visited[i] = False
f()
