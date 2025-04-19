import sys
input = sys.stdin.readline

def min_cal():
    nums = input().strip().split('-')
    res = sum(map(int, nums[0].split('+')))
    for num in nums[1:]:
        res -= sum(map(int, num.split('+')))
    print(res)
min_cal()