# # TODO Напишите код для проверки возраста

# age = int(input("Введите ваш возраст: "))

# if age < 18:  # TODO Условие для первой категории
#     print("Вам ещё рано!")
# elif 18 < age < 65:  # TODO Условие для второй категории
#     print("Добро пожаловать!")
# else:
#     print("Берегите здоровье!")

# TODO Найдите сумму чётных чисел

# start = 1  # Начало диапазона
# end = 20  # Конец диапазона

# # TODO Используйте цикл для нахождения суммы
# sum_even = 0
# for i in range(start,end+1):
#     if i%2==0 :
#         sum_even += i

# print(f"Сумма чётных чисел от {start} до {end}: {sum_even}")

# TODO Найдите количество книг, которое можно разместить на дискете

# print(f"Количество книг, помещающихся на дискету:{(1.44*10**6)//(100*50*25*4)}")

# TODO Создайте словарь с ценами товаров

# prices = {
#     "яблоко": 50,
#     "банан": 30,
#     "апельсин": 70,
#     "груша": 100
# }

# product = input("Введите название товара: ")

# # TODO Проверьте наличие товара в словаре
# if product in prices:
#     print(f"Цена на {product}: {prices[product]} руб.")
# else:
#     print("Такого товара нет в списке.")

# TODO Реализуйте функцию расчёта расстояния

# import math

# def calculate_distance(x1, y1, x2, y2):
#     return math.sqrt((x1-x2)**2+(y1-y2)**2)  # Формула расчёта

# # Пример вызова функции
# x1, y1 = 0, 0
# x2, y2 = 3, 4

# distance = calculate_distance(x1, y1, x2, y2)
# print(f"Расстояние между точками: {distance:.2f}")

# def celsius_to_fahrenheit(c):
#     return round(9/5*c+32,2)

# def fahrenheit_to_celsius(f):
#     return round(5/9*(f-32),2)
# while True:
#     choice = input("Выберите перевод (1: Цельсий -> Фаренгейт, 2: Фаренгейт -> Цельсий): ")

#     if choice == "1" :
#         c = int(input('Введите температуру в цельсиях'))
#         print(celsius_to_fahrenheit(c))
#         break
    
#     elif choice == "2" :
#         f = int(input('Введите температуру в фаренгейтах'))
#         print(fahrenheit_to_celsius(f))
#         break
#     else :
#         print("Введите 1 или 2")
#         continue
        
# TODO Реализуйте вычисление факториала

# number = int(input("Введите число: "))

# factorial = 1
# for i in range(1,number+1):
#     factorial *=i

# print(f"Факториал числа {number}: {factorial}")

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import fsolve

# # Определение функций
# def f1(x):
#     return x**3-x

# def f2(x):
#     return 2*x-1

# # Разница функций для нахождения пересечений
# def diff(x):
#     return f1(x) - f2(x)

# # Нахождение точек пересечения
# x_roots = fsolve(diff, [-2, 0, 2])  # Три предположительных корня
# y_roots = f1(x_roots)

# x = np.linspace(-3,3,100)
# plt.plot(x,f1(x),color='blue',label='f1(x)')
# plt.plot(x,f2(x),color='red',label='f2(x)')
# plt.scatter(x_roots,y_roots,color='black',label='Точки пересечения')
# plt.xlim(-3,3)
# plt.ylim(f2(-3),f1(3))
# plt.grid()
# plt.legend()
# plt.title('Graphing')
# plt.show()

# import numpy as np
# import math
# import matplotlib.pyplot as plt
# from scipy.optimize import fsolve

# def f1(x):
#     return np.sin(x)
# def f2(x):
#     return np.cos(x)

# x = np.linspace(0,2*math.pi,100)
# x_roots1 = fsolve(f1,[0,3,6])
# x_roots2 = fsolve(f2,[1.5,4.5])
# plt.plot(x,f1(x),label='f1(x)=sinx')
# plt.plot(x,f2(x),label='f2(x)=cosx')
# plt.scatter(x_roots1,f1(x_roots1),label='корни син')
# plt.scatter(x_roots2,f2(x_roots2),label='корни кос')
# plt.xlim(0,2*math.pi+1)
# plt.ylim(-1.5,1.5)
# plt.grid()
# plt.legend()
# plt.show()