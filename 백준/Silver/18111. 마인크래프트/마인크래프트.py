import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
lst = []
min_num = 256
avg = 0

for _ in range(N):
    check_lst = list(map(int, input().split()))
    lst.append(check_lst)
    min_num = min(min_num, min(check_lst))
    avg += sum(check_lst)

check = int((avg / (N * M)) + 0.5)

res_1 = 10**9
res_2 = 0
res_time, res_height = 10**9, 0

def check_f():
    global res_1, res_2

    for target in range(min_num, 257):
        minus_num, plus_num = 0, 0

        for i in range(N):
            for j in range(M):
                check_num = lst[i][j] - target
                if check_num > 0:
                    minus_num += check_num
                else:
                    plus_num -= check_num

        if minus_num + B >= plus_num:
            time = minus_num * 2 + plus_num
            if time < res_1 or (time == res_1 and target > res_height):
                res_1, res_height = time, target

    for i in range(N):
        for j in range(M):
            res_2 += (lst[i][j] - min_num) * 2


    if res_1 == res_2:
        print(res_1, max(res_height, min_num))
    else:
        if res_1 < res_2:
            print(res_1, res_height)
        else:
            print(res_2, min_num)

check_f()
