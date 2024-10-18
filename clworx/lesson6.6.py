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