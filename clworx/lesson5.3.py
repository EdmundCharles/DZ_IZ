import math
a = 2
b = 4
r = 2
count = 0
def proverka(x,y) :
    if math.sqrt((a-x)**2+(b-y)**2) < r :
        print(x,y)
p1 , p2 = 1  , 4
for i in 