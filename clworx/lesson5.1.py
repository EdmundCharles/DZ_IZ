from random import randint
len = int(input())
lst = [round(randint(0,100),2) for x in range(len)]

def swap(lst) :
    print('Source', lst)
    print('length', len)
    a = lst.pop(0)
    b = lst.pop(-1)
    lst.insert(0,b)
    lst.append(a)
    print('changed', lst)
swap(lst)