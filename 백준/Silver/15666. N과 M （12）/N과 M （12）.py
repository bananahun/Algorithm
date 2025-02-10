import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(set(map(int, input().split())))
res = []

def nmnm(start):
    if len(res) == m:
        print(*res)
        return
    for i in range(start, len(lst)):
        res.append(lst[i])
        nmnm(i) 
        res.pop()

nmnm(0)
