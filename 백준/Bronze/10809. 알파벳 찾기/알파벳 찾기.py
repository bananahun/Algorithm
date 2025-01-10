word = input()
check = 'abcdefghijklmnopqrstuvwxyz'
res = [-1] * 26

for i in range(len(word)):
    for j in range(len(check)):  
        if word[i] == check[j] and res[j] == -1:  
            res[j] = i 
            break

print(*res)
