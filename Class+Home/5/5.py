import math
from random import randint


def gipotenuza(x, y):
    return math.sqrt(x**2+y**2)


def random_kateti():
    return [round(randint(1, 1000), 2) for m in range(1, 3)]


gipotenuze = []
for i in range(1, 3):
    print(f'Generated {i} triangle..')
    a, b = random_kateti()
    print(f'{a}, {b}, ~{round(gipotenuza(a, b), 3)}')
    gipotenuze.append(gipotenuza(a, b))
if gipotenuze[0] > gipotenuze[1]:
    print('And 1 gipotenuza is the longest')
elif gipotenuze[0] < gipotenuze[1]:
    print('And 2 gipotenuza is the longest')
else:
    print("Somehow the gipotenuzas are equal")
