# import sys
# input = sys.stdin.readline

# def fff(xy):
#     res = 0
#     x1, y1, x2, y2 = xy
#     for i in range(x1 - 1, x2):
#         for j in range(y1 - 1, y2):
#             res += lst[i][j]  
#     print(res)
# n, m = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]
# lst_xy = [list(map(int, input().split())) for _ in range(m)]

# for xy in lst_xy:
#     fff(xy)
'''
시간 초과 날줄 알았음
근데 다르게 어떻게 풀라는건지 잘 모르겠음ㅋㅋ
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)