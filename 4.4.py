#4. Представлен список чисел. Определить элементы списка,
#не имеющие повторений. Сформировать итоговый массив чисел,
#соответствующих требованию. Элементы вывести в порядке их
#следования в исходном списке. Для выполнения задания обязательно
#использовать генератор.

old_list = [1, 3, 4, 5, 675, 34, 2, 4, 675, 7, 1, 4]
new_list =[el for el in old_list if old_list.count(el) == 1]
print(new_list)