# import sys
# input = sys.stdin.readline

# '''
# a -> b
# 최소로 가는 방법 구하기
# 방법은 2가지 방법이 존재한다.
# 숫자의 오른쪽에 1을 붙이기 or 2를 곱하기

# ### 100 40021
# ### 5

# 거꾸로 가보자 
# 100에서 40021 을 만들지 말고 40021에서 100을 만들어 보자. 끝에 1을 더한다는건 1을 빼고 10으로 나눴을 때 나누어 떨어져야함. 
# 왜냐 자릿수가 바뀌니까
# '''
# def plus(num_1):
#     res_1 = str(num_1)+'1'
#     return int(res_1)

# def multiply(num_2):
#     return num_2 * 2

# a, b = map(int, input().split())
# lst = []
# res = 1
# while a!= b:
#     res += 1
#     check = b
#     if b % 10 == 1:
#         b //= 10
#     elif b%2 == 0:
#         b //= 2
#     if check == b:
#         print(-1)
#     if a == b:
#         break

# print(res)

import sys
from collections import deque

input = sys.stdin.readline

def plus(num_1):
    res_1 = str(num_1)+'1'
    return int(res_1)

def multiply(num_2):
    return num_2 * 2

a, b = map(int, input().split())

queue = deque([(a, 1)])

while queue:
    num, count = queue.popleft()

    if num == b:
        print(count)
        break

    if multiply(num) <= b:
        queue.append((multiply(num), count + 1))

    if plus(num) <= b:
        queue.append((plus(num), count + 1))
else:
    print(-1)
