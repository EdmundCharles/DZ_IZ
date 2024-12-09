#Task1
n = 3
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
print(r'максимальное во второй строке' ,max(arr[1]))
k = []
for i in range(n):
   k.append(arr[i][2])
print(r'максимальное значение в третьем столбце' ,max(k))
#Task2
n = 3
m = 4
arr = []
for i in range(n):
    brr = []
    for j in range(m):
        brr.append(int(input()))
    arr.append(brr)
print('До замены')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

for i in range(n):
    for j in range(m):
        if arr[i][j] < 0:
            arr[i][j] = 0
        elif arr[i][j] :
            arr[i][j] = 1
print('После замены')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

#Task3
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

#Task4
n = int(input())
arr = []
for i in range(n):
    brr = []
    for j in range(n):
        brr.append(int(input()))
    arr.append(brr)

for i in range(n):
    for j in range(n):
        if j != i:
            if arr[i][j] == arr[j][i]:
                flag = 1
            else :
                flag = 0
                break
if flag == 1 : print('Symmetric!')
else : print('Not symmetric!')
#Task5
n = int(input())
m = int(input())
arr = []
for i in range(n):
    brr = []
    for j in range(m):
        brr.append(int(input()))
    arr.append(brr)
s1 = []
for i in range(n):
    s1.append(sum(arr[i]))
print(arr[s1.index(min(s1))],arr[s1.index(max(s1))])
print(min(s1),max(s1))
#Task6
n = int(input())
m = int(input())
arr = []
for i in range(n):
    brr = []
    for j in range(m):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    k = min(arr[i])
    if k%2 == 0:
        arr[i][arr[i].index(k)] = 0
    else :
        arr[i][arr[i].index(k)] = 1
print(arr)