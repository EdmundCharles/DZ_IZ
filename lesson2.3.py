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