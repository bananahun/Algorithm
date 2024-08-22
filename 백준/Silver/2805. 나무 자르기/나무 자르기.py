import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, tree = map(int, input().split())
lst = list(map(int, input().split()))
start = 1
end = max(lst)
while start <= end:
    mid = (start+end) // 2
    # print(start, end, mid)
    cnt = 0
    for k in lst:
        if k - mid > 0:
            cnt = cnt + k - mid
    if cnt >= tree:
        start = mid + 1
    else:
        end = mid - 1
print(start - 1)