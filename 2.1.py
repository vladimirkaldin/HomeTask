#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [123, 123.4, '123', 'abc', None, True, False, (123, 213), {123: 'ert'}, {123, 'ert'}]

for i in my_list:
    print(type(i))
    i =+ 1
