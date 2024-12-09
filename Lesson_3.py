#Task1(Class)
n = input("Введите цену за килограмм конфет \n")
count = 0
for i in range(1,11) :
    count +=1
    s = float(n)*i
    print(f'{count} килограмм конфет стоит {s} рублей')
#Task2(Class)
x = int(input("Введите количество чисел в последовательности \n"))
i = 0
s = 0
while x > 0 :
    s +=x 
    i +=1
    print(i)
    x -=1
print(s)
#Task3(Class)
def is_num(z):
    try:
        int(z)
        return True
    except ValueError:
        return False


x = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
nums = []
for i in x:
    if is_num(i):
        nums.append(int(i))
print(sum(nums))

#Task1(Home)
n = int(input("Enter a number up to 100 \n"))
if n > 100 :
    print("-_-")
else :
    sum = 0
    while n > 0 :
        sum += n**3
        n -= 1
    print(f'sum is {sum}')
#Task2(Home)
a = 1
while a < 10:
    b = 1
    while b < 10:
        print((a * b), end="\t")
        b += 1
    print()
    a += 1
