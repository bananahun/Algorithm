import sys
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

res_0, res_1 = 0, 0

def check(y, x, num):
    global res_0, res_1
    color = lst[y][x]
    for i in range(y, y + num):
        for j in range(x, x + num):
            if lst[i][j] != color:
                half = num // 2
                check(y, x, half)
                check(y + half, x, half)
                check(y, x + half, half)
                check(y + half, x + half, half)
                return
    if color == 0:
        res_0 += 1
    else:
        res_1 += 1

check(0, 0, N)
print(res_0, res_1)
