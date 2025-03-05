import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

res = [0] * (N + 1)
for idx in range(N):
    res[idx + 1] = res[idx] + lst[idx]

for _ in range(M):
    a, b = map(int, input().split())
    print(res[b] - res[a - 1])