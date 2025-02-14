import sys
input = sys.stdin.readline

'''
모든 집에 칠하는 최솟값을 구하시오

빨강 or 초록 or 파랑 -> 최솟값을 구하시오

dp 를 이용해서 한번 풀어보자
기본적으로 가장 작은 값을 기준으로 적어가고
그리고 나올수 있는 다른 경우를 계속 해서 저장을 해나가는거지.
뭔말인지 알겠찌?? 나는 잘 모르겠다.

3
26 40 83
49 60 57
13 89 99


'''
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3] * n

dp = [[0] * 3 for _ in range(n)]
dp[0] = lst[0]

for i in range(1, n):
    dp[i][0] = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = lst[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))

