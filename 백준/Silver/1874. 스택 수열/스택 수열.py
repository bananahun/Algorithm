cnt = 1
check = True
stack = []
res = []

N = int(input())
for i in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        check = False
        break
if check == False:
    print("NO")
else:
    for i in res:
        print(i)