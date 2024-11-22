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