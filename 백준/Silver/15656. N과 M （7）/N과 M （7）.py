n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def rrr():
    if len(res) == m:
        # print(res)
        for numm in res:
            print(numm)
        return
    for num in arr:
        # print(num)
        res.append(num)
        rrr()
        res.pop()

rrr()