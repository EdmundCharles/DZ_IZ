n = input("Введите цену за килограмм конфет \n")
count = 0
for i in range(10) :
    count +=1
    s = float(n)*i
    print(f'{count} килограмм конфет стоит {s} рублей')