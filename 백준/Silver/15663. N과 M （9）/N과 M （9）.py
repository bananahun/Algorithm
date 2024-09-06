n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * n
res = []

def rrr():
    check = 0
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        if check != num[i] and visited[i] == 0:
            res.append(num[i])
            visited[i] = 1
            check = num[i]
            rrr()
            res.pop()
            visited[i] = 0

rrr()