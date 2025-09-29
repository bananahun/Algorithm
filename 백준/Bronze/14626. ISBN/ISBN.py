import sys
input = sys.stdin.readline

ISBN = input().strip()

check_sign = int(ISBN[-1])

temp = 0
unknown = 0

for number, weight in zip(ISBN[:-1], [1, 3] * 6):
    if number == '*':
        unknown = weight
        continue

    temp += int(number) * weight

for unknown_number in range(10):
    rest = (temp + (unknown_number * unknown) + check_sign) % 10
    
    if rest == 0:
        print(unknown_number)
        break