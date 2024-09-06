n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []
idx = 0  

def rrr():
    global idx  
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(idx, n):
        res.append(arr[i])
        idx = i  
        rrr()
        res.pop()
    idx = 0  

rrr()
