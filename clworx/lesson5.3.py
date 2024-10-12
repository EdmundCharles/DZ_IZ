import math
count = 0
p = [1, 200]
f = [3, 4]
l = [5, 7]
tochkiez = [p, f, l]
a, b, r = 2, 3, 5


def check(list):
    global count
    if math.sqrt((a-list[0])**2 + (b - list[1])**2) <= r:
        print(f'{list}, inside')
        count += 1
    else:
        print(f'{list}, outside')


for i in tochkiez:
    check(i)
print(count)
