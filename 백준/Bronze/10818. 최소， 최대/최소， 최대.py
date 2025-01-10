num = int(input())
arr = list(map(int,input().split()))
minn = arr[0]
maxn = arr[0]
for check in arr:
    if check > maxn:
        maxn = check
    elif check < minn:
        minn = check
print(minn, maxn) 
