import sys
input = sys.stdin.readline

'''
분할 및 재귀가 필요한 문제다.
기본적으로 4분면 기준으로 계속 해서 나누는걸 반복 
-> 가장 작은 바운더리 안에 들어오면 거기선 찾기?!?!
일단 처음 칸의 갯수에서 4로 나눠서 한번 생각해보자
일단 
3 7 7 일때로 예를 들어 보면 
가로 세로 8칸인데 7 7 이 어디 들어가느냐를 생각해보면 우선 
'''
time = 0
def check(N, a, b):
    global time
    if N == 0:
        return 0
    size = 2 ** (N-1)
    area = size * size
    time += 1
    # print(time,'번',a, b, size, N)
    if a < size and b < size:
        return check(N-1, a, b)
    elif a < size and b >= size:
        return area + check(N-1, a, b-size)
    elif a >= size and b < size:
        return 2 * area + check(N-1, a - size, b)
    else:
        return 3 * area + check(N-1, a - size, b - size)

N, a, b = map(int, input().split())

print(check(N, a, b))