#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, year_of_birth, city, email, cellplone):
    print(f'Пользователь {name} {surname}, родился в {year_of_birth} году, проживает в городе {city}. Контактные данные: e-mail {email}, телефон {cellplone}')

user(name='Владимир', surname='Калдин', year_of_birth='1990', city='Москва', email='vladimirkaldin@mail.ru', cellplone='+79850882523')