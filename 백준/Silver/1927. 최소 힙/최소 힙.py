# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = []

# for _ in range(N):
#     num = int(input())

#     if num == 0:
#         if lst:
#             print(lst.pop(0))
#         else:
#             print(0)
#     else:
#         lst.append(num)
#         lst.sort() 
import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
