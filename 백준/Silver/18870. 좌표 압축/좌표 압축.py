import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst_sorted = sorted(set(lst))
'''
6
1000 999 1000 999 1000 999
-> 
lst 는 똑같이 나오고
겹치는거랑 뺴고 정렬해서
[999, 1000]
여기서 이제 기존에 만든 리스트 에서 빼주는거지
근데 리스트로 하면 n^2 이라서 시간초과가 나는데
딕셔너리를 쓴다면? 
시간 초과를 줄일수 있지 않을까?
그럼 리스트 값을 딕셔너리의 키값으로 넣고
내가 새로 만들어준 세트를 돌려서 
5
2 4 -10 4 -9
정렬 리스트
[-10, -9, 2, 4]
근데 생각해보면 그냥 작은것 순서대로 각각의 인덱스 값을 뽑아 내면 되는거자나??
그래서 그걸 딕셔너리로 넣어주기만 하면?? 끝
'''

lst_dict = {value: index for index, value in enumerate(lst_sorted)}
# print(lst_dict)
# print(lst_sorted)
res_lst = []

for i in lst:
    res_lst.append(lst_dict[i])

print(*res_lst)
