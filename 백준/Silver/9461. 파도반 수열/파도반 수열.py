import sys
input = sys.stdin.readline

T = int(input())
'''
1 1
1 1
1 1 
2 1+1
2 1+1
3 1+2
4 1+3
5 1+4
7 2+5
9 2+7
12 3+9
16 4+12
n n-1 n-5

6 -> 3
12 -> 16

'''
for _ in range(T):
    n = int(input())
    dp = [False] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    if n <= 5:
        print(dp[n])
    else:
        for i in range(6, n+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[n])
