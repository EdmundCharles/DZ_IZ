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