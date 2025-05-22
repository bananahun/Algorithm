import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

l_idx = 0
r_idx = N - 1

best_sum = float('inf')
answer = (0, 0)

while l_idx < r_idx:
    total = lst[l_idx] + lst[r_idx]
    if abs(total) < abs(best_sum):
        best_sum = total
        answer = (lst[l_idx], lst[r_idx])

    if total < 0:
        l_idx += 1
    elif total > 0:
        r_idx -= 1
    else:
        break 
print(*answer)
