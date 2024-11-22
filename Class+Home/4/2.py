s = input()
a = ''
count = 0
for i in s :
    if i == ':' :
        count += 1
        a = (a + '%')
    else :
        a = (a + i)
print(a)
print(f'Количество замен : {count}')