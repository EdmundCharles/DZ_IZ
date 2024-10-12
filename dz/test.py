def armstr(x) :
    x = str(x)
    s = []
    for i in x :
        s.append(i)
    s = list(map(int, s))
    sum = 0
    for i in s :
        sum += i*len(x)
    print(sum)
armstr(1234)



x = '1234'
print(len(x))