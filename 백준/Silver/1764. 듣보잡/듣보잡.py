N, M = map(int, input().split())
arr1= set()
arr2= set()

for _ in range(N):
    arr1.add(input())
for _ in range(M):
    arr2.add(input())

result = sorted(set(arr1&arr2))

print(len(result))
for name in result:
    print(name)