n = 2
lst = []
for i in range(3,100) :
    while i%n !=0:
        n+=1
    if n == i :
        lst.append(i)
print(lst)