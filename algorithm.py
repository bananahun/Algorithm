# def fibonacci (num):
#     global a, b
#     if num == 0:
#         a += 1
#         return num==0
#     elif num == 1:
#         b += 1
#         return num==1
#     else:
#         value = fibonacci(num-1) + fibonacci(num-2) 
#         return value
    
# T = int(input())
# for _ in range(T):
#     a, b = 0, 0
#     num = int(input())
#     fibonacci(num)
#     print(a,'',b)

T = int(input())

for _ in range(T):
    num = int(input())
    res1, res2 = 1, 1
    if num == 0:
        res1 = 1
        res2 = 0
        print(res1,res2)   
    elif num == 1:
        res1 = 0
        res2 = 1
        print(res1,res2)
    else: 
        for _ in range(num-2):
            res1, res2 = res2 , res1 + res2
        print(res1,res2)


# 피보나치 수열 값 예시 들어보기
# ex) 
# 22 -> 21 + 20
# 0 -> 0, 0
# 1 -> 0, 1
# 2 -> 1, 1
# 3 -> 1, 2
# 4 -> 2, 3
# 5 -> 3, 5
# 6 -> 5, 8
