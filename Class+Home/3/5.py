n = int(input("Enter a number up to 100 \n"))
if n > 100 :
    print("-_-")
else :
    sum = 0
    while n > 0 :
        sum += n**3
        n -= 1
    print(f'sum is {sum}')