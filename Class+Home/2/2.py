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
