import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int, input().split()))
lst.sort()
res = []

def nmnm():
    if len(res) == m:
        print(*res)
        return
    for i in lst:
        if i not in res:
            res.append(i)
            nmnm()
            res.pop()

nmnm()
