from random import *
N = int(input("Введите количство чисел в массиве :"))
s = [randint(0,10000000000000) for x in range(N)]
print(f'{min(s)} - минимальное число в случайно сгенерированном массиве из {N} чисел')
print(f'{s.index(min(s))} - его индекс в этом массиве')
