# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
print("Задача 1")
print("Давайте решим уравнение y = ax2 + bx + c?")
solve_eq = input("y / n: ")
if solve_eq == "y":
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    x = float(input("Задайте точку x: "))
    y = a * x ** 2 + b * x + c
    print(y)
elif solve_eq == "n":
    print("Завершено.")
else:
    print("Неизвестная команда")

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
print("")
print("Задача 2")
d = int(input("Введите целое число: "))
print("Ваше число + 2 = ", d + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print("")
print("Задача 3")
age = int(input("Полных лет: "))
if age >= 18:
    print("Доступ разрешён")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
