res = []
for _ in range(10):
    check = int(input())
    res.append(check%42)
print(len(set(res)))
