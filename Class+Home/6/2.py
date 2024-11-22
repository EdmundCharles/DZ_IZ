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
