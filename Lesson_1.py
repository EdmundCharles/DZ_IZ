# Task1
import math
r = int(input("Whats the radius,cm? \n"))
print(f' The length is {round(2*math.pi*r, 2)} cm, the square is {round(math.pi*r**2, 2)} cm*2')

# Task2
x, y = 10, 55
print(x, y)
x, y = y, x
print(x, y)

# Task3
L = input("Enter string length, m \n")
print(round(2*math.pi*(math.sqrt(float(L)/9.81)), 4))
