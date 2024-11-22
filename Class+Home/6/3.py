n = int(input())
arr = []
for i in range(n):
    brr = []
    for j in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
s1 = []
for i in range(n):
    s1.append(sum(arr[i]))
s2 = []
for i in range(n) :
    summa = 0
    for j in range(n):
        summa += arr[j][i]
    s2.append(summa)
if len(set(s1)) == 1:
    if len(set(s2)) == 1:
        if set(s1) == set(s2):
            print('Magic sqare!')
else :
    print('Not a magic one!')
