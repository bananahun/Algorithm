import sys
input = sys.stdin.readline
'''
4 2
9 7 9 1

-> 1 7 9 9

1 7
1 9
7 9
9 9

 
'''
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * n
res = []
def f(s):
    if len(res) == m:
        print(*res)
        return
    check = 0
    for i in range(s, n):
        if visited[i] == False and lst[i] != check:
            visited[i] == True
            res.append(lst[i])
            check = lst[i]
            f(i+1)
            res.pop()

f(0)