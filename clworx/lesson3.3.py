def is_num(z) :
    try :
        int(z)
        return True
    except ValueError:
        return False
x = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
m = list(filter(is_num , x))
n = list(map(int,m))
while x == range(max(n))