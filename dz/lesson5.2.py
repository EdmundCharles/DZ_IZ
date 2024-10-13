def poly(x):
    x = bin(x)
    x = x[2:]
    for i in range(len(x)//2) :
        if x[i] == x[-1-i]:
            flag = True
        else :
            flag = False
            break
    return flag 

def odd(l):
    s = []
    for i in range(3,l+1):
        s.append(i)
                 
    def odder(j) :
        n = 2
        while j%n != 0 :
            n += 1
        return n 
    odds=[]
    for i in s :
        if odder(i) == i:
            odds.append(i)
    return odds

l = int(input("Введите диапазон - от 0 до :"))
s = []
for i in odd(l):
    if poly(i) :
      s.append(i)
print(*s)  