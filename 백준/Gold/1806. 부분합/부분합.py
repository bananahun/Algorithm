import sys
input = sys.stdin.readline

'''
10 15
5 1 3 5 10 7 4 9 2 8
연속한 수의 합을 구해서 해당 숫자가 15가 되도록 만들어야함.
만들수 있는 모든 경우중 가장 짧은 이어지는 숫자의 합을 구하자.
흐음 모든 경우를 다 확인해야할까...?? 부분합이니까 이것도 투 포인터로?
'''

N, tar = map(int, input().split())
lst = list(map(int, input().split()))

res = int(10000000)
l = 0
check = 0

for r in range(N):
    check += lst[r]
    while check >= tar:
        res = min(res, r - l + 1)
        check -= lst[l]
        l += 1

if res != 10000000:
    print(res)
else:
    print(0)