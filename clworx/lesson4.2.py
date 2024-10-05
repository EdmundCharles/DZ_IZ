s = input()
a = ''
count = 0
for i in range(len(s)) :
    if s[i] == ':' :
        count += 1
        a = (a + '%')
    else :
        a = (a + s[i])
print(a)
print(f'Количество замен : {count}')