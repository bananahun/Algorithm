import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dq = deque([i+1 for i in range(N)])

res = []
while dq:
    dq.rotate(-(K-1))
    res.append(dq.popleft())

print("<" + ", ".join(map(str, res)) + ">") 
