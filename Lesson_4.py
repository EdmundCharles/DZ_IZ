#Task1(Class)
s = input()
s = ' ' + s
print(s.count(' е'))
#Task2(class)
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
#Task3(Class)
s = input()
count = s.count('.')
s = s.replace('.','')

print(f'Symbols replaced {count} , result: \n {s}')
#Task4(class)
s = list(input().split(' '))
for i in s :
    s.pop(0)
    for j in s :
        if int(i)*int(j) > 0 and int(i)+int(j) < 0 :
            print(i , j)
#Task5(class)
from random import *
N = int(input("Введите количство чисел в массиве :"))
s = [randint(0,10000000000000) for x in range(N)]
print(f'{min(s)} - минимальное число в случайно сгенерированном массиве из {N} чисел')
print(f'{s.index(min(s))} - его индекс в этом массиве')

#Task6(class)
from random import *
x = []
s = [randint(0,20) for x in range(9)]
print(s)
for i in s :
    if i<15 :
        x.append(i*2)
    else :
        x.append(i)
print(x)
#Task1(Home)
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
#Task2(Home)
s = "wejwdwjnf(jdnjdnvjdnvj)sdkjfei"
i = s.find("(")
j = s.find(")")
print(s[i+1:j])
#Task3(Home)
s = 'аллея бенго авляция сокет адгезия сон авиация кукуха абразия едет'
s = s.split(" ")
glagol = []
for i in s:
    if i.startswith("а") and i.endswith("я"):
        glagol.append(i)
print(*glagol)
