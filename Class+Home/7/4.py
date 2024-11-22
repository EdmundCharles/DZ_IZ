import os
name = str(input("Name your file\n"))+'.txt'
file = open(name,'w')
flag = 1
while flag == 1 :
    n = str(input('Enter stroka\n'))
    file.write(n + '\n')
    if len(n) == 0:
        flag = 0
file.close()
