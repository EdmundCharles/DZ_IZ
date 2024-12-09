#Task1
a, b, c = input("Введите целые числа через пробел \n").split()
if not a.isdigit() or not b.isdigit() or not c.isdigit():
    print('Вводите только целые числа')
else:
    if a<b and a<c :
        print(a,'наименьшее')
    else :
        if b<c :
            print(b , 'наименьшее')
        else :
            print(c , 'наименьшее')     
    if 1<=int(a)<=3 :
        print(a,'принадлежит [1;3]')
    if 1<=int(b)<=3 :
        print(b,'принадлежит [1;3]')
    if 1<=int(c)<=3 :
        print(c,'принадлежит [1;3]')    

#Task2
def is_number(z):
    try:
        float(z)
        return True
    except ValueError:
        return False


x, y = input("Введите два числа, которые необходимо поделить, через пробел \n").split()
m = [x,y]
if len(m) == 2:
    if is_number(x) and is_number(y):
        if float(y) == 0:
            print("На ноль делить нельзя")
        else:
            x, y = map(float, (x, y))
            print(f'{x}/{y} = {x/y}')
    else:
        print('Вводите числа!')
else:
    print('Введите ДВА числа!')

#Task3
def is_number(z) :
    try :
        float(z)
        return True
    except :
        return False
x = input("Введите сумму покупки \n")
if is_number(x) and float(x) > 0 :
    x = float(x)
    if x > 20 :
        print(f'Стоимость покупки с учетом скидки в размере {round(0.35*x,2)} - {round(x*0.65,2)}')
    else :
        print(f'Стоимость покупки {round(x,2)},скидка предоставляется только при сумме более 20') 
else :
    print('Невозможная стоимость покупки!')   
#Task4
m = input("Enter month's number: from 1 to 12 \n")
if m.isdigit() and 1<=int(m)<=12 :
    m = int(m)
    if 3<=m<=5 :
        print('Spring')
        if m==3:
            print('March')
        elif m==4 :
            print('April')
        else :
            print('May')    
    elif 6<=m<=8 :
        print('Summer')
        if m==6 :
            print('June')
        elif m==7 :
            print('July')
        else :
            print('August')
    elif 9<=m<=11 :
        print('Autumn')
        if m==9 :
            print('September')
        elif m==10 :
            print('October')
        else :
            print('November')
    else :
        print('Winter')
        if m==1 :
            print('January')
        elif m==2 :
            print('February')
        else :
            print('December')      
else :
    print('Please, enter correct values.')