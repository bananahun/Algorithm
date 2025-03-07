import sys
input = sys.stdin.readline

'''
2*n 의 타일을
2*1 내지 1*2 의 타일로 채우는 방법의 수를 구하여라
이것도 기본적으로 dp 점화식을 생각해봐야 할거 같다.

1 1
2 2
3 3
4 5
5 8
6 13
7 21
8 34
9 55
'''
N = int(input())
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)

