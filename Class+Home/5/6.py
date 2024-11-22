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