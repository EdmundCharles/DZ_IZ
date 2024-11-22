s = list(input().split(' '))
for i in s :
    s.pop(0)
    for j in s :
        if int(i)*int(j) > 0 and int(i)+int(j) < 0 :
            print(i , j)