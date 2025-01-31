import sys
input = sys.stdin.readline

word_dict = {}  # `dict` 대신 다른 변수명 사용
index_dict = {}  # 인덱스를 저장하는 별도 딕셔너리
N, M = map(int, input().split())

for i in range(1, N + 1):  # 1부터 시작
    word = input().strip()
    word_dict[word] = i  # 단어를 키, 인덱스를 값으로 저장
    index_dict[i] = word  # 인덱스를 키, 단어를 값으로 저장

for _ in range(M):
    check = input().strip()
    if check.isdigit():  # 숫자 여부 확인
        print(index_dict[int(check)])  # 숫자이면 인덱스로 단어 조회
    else:
        print(word_dict[check])  # 문자열이면 인덱스 조회
