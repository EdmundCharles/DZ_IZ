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