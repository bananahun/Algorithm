import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    # n이 1인 경우를 처리
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    
    # dp 초기 값 업데이트
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    
    # 2부터 n-1까지 계산
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    # 마지막 위치에서 최대값 출력
    print(max(dp[0][n-1], dp[1][n-1]))
