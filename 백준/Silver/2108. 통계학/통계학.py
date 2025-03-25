import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

mean = round(sum(nums) / n)
median = nums[n // 2]

dict = {}
maxx = 0

for num in nums:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
    maxx = max(maxx, dict[num])

modes = [k for k, v in dict.items() if v == maxx]
modes.sort()

mode = modes[1] if len(modes) > 1 else modes[0]
res = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(res)
