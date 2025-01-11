def changing(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    else:
        return num


arr = []
for _ in range(3):
    check = input()
    if check == 'Fizz' or check == 'Buzz' or check == 'FizzBuzz':
        arr.append(-1)
    else:
        arr.append(int(check))

res = 0

if arr[0] != -1:
    res = arr[0]+3
    # print(arr[0]+3)
elif arr[1] != -1:
    res = arr[1]+2
    # print(arr[1]+2)
elif arr[2] != -1:
    res = arr[2]+1
    # print(arr[2]+1)
print(changing(res))

