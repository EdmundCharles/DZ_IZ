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