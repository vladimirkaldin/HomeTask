#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * my_func(x, y - 1)
    elif y < 0:
        return (1 / (x * my_func(x, abs(y) - 1)))

print(my_func(2, -10))