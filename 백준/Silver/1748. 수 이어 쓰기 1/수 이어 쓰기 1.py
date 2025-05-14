import sys
input = sys.stdin.readline

n = int(input())
length = 0
digit = 1
start = 1

while start * 10 <= n:
    length += (start * 10 - start) * digit
    digit += 1
    start *= 10

length += (n - start + 1) * digit
print(length)
