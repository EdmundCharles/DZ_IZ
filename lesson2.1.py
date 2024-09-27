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