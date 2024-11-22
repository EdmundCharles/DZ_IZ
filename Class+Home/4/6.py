from random import *
x = []
s = [randint(0,20) for x in range(9)]
print(s)
for i in s :
    if i<15 :
        x.append(i*2)
    else :
        x.append(i)
print(x)