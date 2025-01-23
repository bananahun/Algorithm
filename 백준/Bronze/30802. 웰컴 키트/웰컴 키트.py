import sys

input = sys.stdin.readline

N = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())
'''
23 # people #
3 1 4 1 5 9 # size #
5 7 # t, pen#
###
7
3 2
###
'''
res1 = 0
res2 = 0
res3 = 0
for _ in range(6):
    shirt = shirts.pop()
    if shirt == 0:
        res1 += 0
    elif (shirt % t) == 0:
        res1 += (shirt // t)
    else: 
        res1 += ((shirt // t)+1)

res2 = N // p
res3 = N % p
print(res1)
print(res2, res3)