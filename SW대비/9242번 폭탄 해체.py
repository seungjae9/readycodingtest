# 9242번 폭탄 해체
bomb = [
        ['*', '*', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' '],
        [' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' '],
        ['*', '*', '*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' '],
        ['*', '*', '*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', ' '],
        ['*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' '],
        ['*', '*', '*', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', ' '],
        ['*', '*', '*', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' '],
        ['*', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' '],
        ['*', '*', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' '],
        ['*', '*', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' '],
        ]

code = []
for i in range(5):
    code.append(list(input() + " "))
res = []
for i in range(len(code[0]) // 4):
    res.append([])

temp = ""
for i in range(len(code)):
    check = 0
    inn = 0
    for j in range(len(code[i])):
        temp += code[i][j]
        check +=1
        if check == 4:
            res[inn] += temp
            inn += 1
            check = 0
            temp = ""
ans = 0
number = ""
for i in range(len(res)):
    for j in range(10):
        if res[i] == bomb[j]:
            number += str(j)
            ans += 1

if ans == len(code[0]) // 4 and int(number) % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")

