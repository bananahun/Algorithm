import sys
input = sys.stdin.readline

n = int(input())

res = []

for _ in range(n):
    num = int(input())
    if num == 0:
        res.pop()
    else:
        res.append(num)

print(sum(res))
