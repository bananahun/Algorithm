import sys
from collections import Counter

input = sys.stdin.readline

N, M, B = map(int, input().split())
block_dict = Counter()

min_num, max_num = 256, 0

for _ in range(N):
    row = list(map(int, input().split()))
    for height in row:
        block_dict[height] += 1
        min_num = min(min_num, height)
        max_num = max(max_num, height)

res_time = float('inf')
res_height = 0

# 전체 블록 개수
total_blocks = sum(height * count for height, count in block_dict.items())

for target in range(min_num, max_num + 1):
    remove_blocks = sum((height - target) * block_dict[height] for height in block_dict if height > target)
    add_blocks = sum((target - height) * block_dict[height] for height in block_dict if height < target)

    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time < res_time or (time == res_time and target > res_height):
            res_time, res_height = time, target

print(res_time, res_height)
