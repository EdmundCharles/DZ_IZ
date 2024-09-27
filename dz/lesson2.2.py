def is_number(z) :
    try :
        float(z)
        return True
    except ValueError:
        return False 
x, y, *m = input("Введите два числа, которые необходимо поделить, через пробел \n").split( )
if len(m) == 0:
    if is_number(x) and is_number(y) :
         x, y = map(float, (x,y))
         print(f'{x}/{y} = {x/y}')    
    else :
         print('Вводите числа!')    
else :
    print('Введите ДВА числа!')