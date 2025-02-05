import sys
input = sys.stdin.readline

def yesorno(check):
    res_1 = 0
    for i in range(len(check)):
        if check[i] == '(':
            res_1 += 1 
        else:
            res_1 -= 1
        if res_1 < 0:
            print('NO')
            return
    print('YES' if res_1 == 0 else 'NO')
            


N = int(input())
for _ in range(N):
    check = input().rstrip()
    yesorno(check)

