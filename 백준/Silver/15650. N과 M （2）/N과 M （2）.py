import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
res = []

def nmnm(start):
    if len(res) == m:
        print(*res)
        return
    for i in range(start,n+1):
        if i not in res:
            res.append(i)
            nmnm(i+1)
            res.pop()

nmnm(1)
