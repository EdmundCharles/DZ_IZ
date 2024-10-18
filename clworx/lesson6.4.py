n = int(input())
arr = []
for i in range(n):
    brr = []
    for j in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(1,n+1):
    for j in range(n):
        if i < j :
            if arr[i][j] == arr[j][i]:
                if 

#нарисовать матрицу 5х5, так как может быть что индексы не свапаются. дальше думай...