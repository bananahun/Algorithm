num = 1
for _ in range(3):
    num = num * int(input())
# print(num)
res = [0] * 10
for check in str(num):
    res[int(check)] += 1
for result in res:
    print(result)