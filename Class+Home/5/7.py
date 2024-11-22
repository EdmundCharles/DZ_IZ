import math 
from random import randint
def proverka_na_vernost(list):
    x , y = list[0] , list[1]
    if x == 0:
        phi = 90
    elif x < 0:
        phi = 180 - math.atan(abs(y/x))
    else :
        phi = math.atan(abs(y/x))
    return phi 
def proverka(k):
    ugol = []
    for j in k :
        ugol.append(proverka_na_vernost(j))
    print(k[ugol.index(min(ugol))],'угол между лучом в эту точку и осью абсцисс наименьший')


s = []
for i in range(0,3) :
    i = [round(randint(0,100),0),round(randint(0,100),0)]
    s.append(i)
print(*s)
proverka(s)