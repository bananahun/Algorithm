def check(txt1, txt2):
    res = []
    txt2_list = list(txt2) 
    for char in txt1:
        if char in txt2_list:
            res.append(char)
            txt2_list.remove(char)
    res = sorted(res)
    print(''.join(res))

while True:
    try:
        text1 = input()
        text2 = input()
        check(text1, text2)
    except:
        break
