import sys
input = sys.stdin.readline

''''
6
10
20
15
25
10
20

-> 3번 연속은 안됨
-> 1칸 내지 2칸 이동 가능
거의 무조건 dp 겠지....?? 각각 한칸씩 올라가면서 최댓값 갱신 하는 방법으로 가볼까

i = max(i-2 + i-3, i-3 i-1) -> 그럼 처음 3개는 미리 정해놓고 시작해야겠구만
'''

N = int(input())
lst = [int(input()) for _ in range(N)]
def check():
    if N == 1:
        return print(lst[0])
    elif N == 2:
        return print(lst[0] + lst[1])
    dp = [0] * (N + 1)
    dp[1] = lst[0]
    dp[2] = lst[0] + lst[1]
    dp[3] = max(lst[0] + lst[2], lst[1] + lst[2])

    for i in range(4, N + 1):
        dp[i] = max(dp[i-2] + lst[i-1], dp[i-3] + lst[i-2] + lst[i-1])
    print(dp[N])

check()



