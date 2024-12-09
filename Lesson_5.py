#Task1(class)
from random import randint
len = int(input())
lst = [round(randint(0,100),2) for x in range(len)]

def swap(lst) :
    print('Source', lst)
    print('length', len)
    a = lst.pop(0)
    b = lst.pop(-1)
    lst.insert(0,b)
    lst.append(a)
    print('changed', lst)
swap(lst)
#Task2(class)
import math

first_frac = input().split()
second_frac = input().split()

def divide(frac_1, frac_2):
  print(f'First frac is {frac_1[0]}/{frac_1[-1]}')
  print(f'Second frac is {frac_2[0]}/{frac_2[-1]}')
  result = [0, 0]
  result[0], result[-1] = float(frac_1[0]) * float(frac_2[-1]), float(frac_2[0]) * float(frac_1[-1])
  # chs, zhm = result
  print(f'Non reduced result is {result[0]}/{result[-1]}')

  def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n

  nod = gcd(result[0], result[-1])

  if result[-1]/nod != 1:
    print(f'Reduced result is {result[0]/nod}/{result[-1]/nod}')
  else:
    print(f'Reduced result is {result[0]/nod}')

divide(first_frac, second_frac)
#Task3(class)
import math
count = 0
p = [1, 200]
f = [3, 4]
l = [5, 7]
tochkiez = [p, f, l]
a, b, r = 2, 3, 5


def check(list):
    global count
    if math.sqrt((a-list[0])**2 + (b - list[1])**2) <= r:
        print(f'{list}, inside')
        count += 1
    else:
        print(f'{list}, outside')


for i in tochkiez:
    check(i)
print(count)

#Task4(class)
from random import randint
count = 0
a = [round(randint(-10000,10000),0) for x in range(round(randint(1,15),0))]
b = [round(randint(-10000,10000),0) for x in range(round(randint(1,15),0))]
c = [round(randint(-10000,10000),0) for x in range(round(randint(1,15),0))]
spisok = [a,b,c]
def deistv(list) :
    sum = 0
    global count   
    for i in list :
        sum += i
    count += 1
    print(f'Сумма элементов массива {count}: {sum}, а его среднее арифметическое:{round(sum/len(list),2)}')
for i in spisok :
    deistv(i)
#Task5(class)
import math
from random import randint


def gipotenuza(x, y):
    return math.sqrt(x**2+y**2)


def random_kateti():
    return [round(randint(1, 1000), 2) for m in range(1, 3)]


gipotenuze = []
for i in range(1, 3):
    print(f'Generated {i} triangle..')
    a, b = random_kateti()
    print(f'{a}, {b}, ~{round(gipotenuza(a, b), 3)}')
    gipotenuze.append(gipotenuza(a, b))
if gipotenuze[0] > gipotenuze[1]:
    print('And 1 gipotenuza is the longest')
elif gipotenuze[0] < gipotenuze[1]:
    print('And 2 gipotenuza is the longest')
else:
    print("Somehow the gipotenuzas are equal")

#Task6(class)
def armstr(x) :
    x = str(x)
    s = []
    for i in x :
        s.append(i)
    s = list(map(int, s))
    sum = 0
    for i in s :
        sum += i**len(x)
    return sum
k = []
for i in range(int(input("Введите диапазон : от 0 до "))) :
    k.append(i)
armstrong_list = []
for j in k :
    if armstr(j) == j :
        armstrong_list.append(j)
print('А вот и все числа Армстронга в указанном промежутке :' , *armstrong_list, 'их всего то', len(armstrong_list),'!')
#Task1(Home)
import math 
from random import randint
def proverka_na_vernost(list):
    x , y = list[0] , list[1]
    if x == 0:
        phi = 90
    elif x < 0:
        phi = 180 - math.atan(abs(y/x))
    else :
        phi = math.atan(abs(y/x))
    return phi 
def proverka(k):
    ugol = []
    for j in k :
        ugol.append(proverka_na_vernost(j))
    print(k[ugol.index(min(ugol))],'угол между лучом в эту точку и осью абсцисс наименьший')


s = []
for i in range(0,3) :
    i = [round(randint(0,100),0),round(randint(0,100),0)]
    s.append(i)
print(*s)
proverka(s)
#Task2(Home)
def poly(x):
    x = bin(x)
    x = x[2:]
    for i in range(len(x)//2) :
        if x[i] == x[-1-i]:
            flag = True
        else :
            flag = False
            break
    return flag 

def odd(l):
    s = []
    for i in range(3,l+1):
        s.append(i)
                 
    def odder(j) :
        n = 2
        while j%n != 0 :
            n += 1
        return n 
    odds=[]
    for i in s :
        if odder(i) == i:
            odds.append(i)
    return odds

l = int(input("Введите диапазон - от 0 до :"))
s = []
for i in odd(l):
    if poly(i) :
      s.append(i)
print(*s)  