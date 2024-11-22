import random

a = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'
s = a.split(" ")
f = [random.choice(s) for x in range(1000)]
stroka = ''
for i in f :
    stroka += i
cur = ''
max = ''
last =''
for i in stroka :
    if i == 'н' and i == last :
        cur += i
        if len(cur)>len(max):
            max = cur 
    else :
        last = i
        cur = i
voskl = ''
for m in range(len(max)) :
    voskl += '!'
stroka = stroka.replace(max , voskl)
print(stroka)
print(max)
print(len(max))