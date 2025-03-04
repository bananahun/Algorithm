import sys
input = sys.stdin.readline

N = int(input())
lst = [[False]*N for _ in range(N)]

x = [False] * N
xy_1 = [False] * (2 * N - 1)
xy_2 = [False] * (2 * N - 1)
result = []

def find(lst):
    for i in range(len(lst)):
        if lst[i] == True:
            return i

def Nqueen(row):
    if row == N:
        check = []
        for i in range(N):
            check.append(find(lst[i]))
            # check.append(lst[i].index(True))
            '''
            여기서 만약에 True가 없다면 ValueError 를 던집니데이~~
            '''
        result.append(check)
        return
    
    for i in range(N):
        if not x[i] and not xy_1[row + i] and not xy_2[row - i + N - 1]:
            lst[row][i] = True
            x[i] = True
            xy_1[row + i] = True
            xy_2[row - i + N - 1] = True
            
            Nqueen(row + 1)
            
            lst[row][i] = False
            x[i] = False
            xy_1[row + i] = False
            xy_2[row - i + N - 1] = False

Nqueen(0)

print(len(result))