# django school пример кода
def sum_number():
    while True:
        number1 = int(input())
        number2 = int(input())
        print(number2 + number1)
        answer = input('Еще раз? ')
        if answer == 'Да':
            print('Продолжим')
            continue
        else:
            print('Подсчет окончен')
            break


# игра угадай число
import random


def game_random_number():
    while True:
        random_number = random.randint(0, 10)
        # нужен для того чтобы дать случайные числа в нужном диапазоне
        # print(random_number)
        user_number = int(input('Введите число: '))
        # воод данных от пользователя
        if user_number == random_number:
            print('Вы выиграли!')
        else:
            print('Вы проиграли!')
        answer = input('Играть еще?')
        if answer == 'Нет':
            break
        elif answer == 'Да':
            continue
        # с данного места цикл начинается снова с самого начала while


# нумерование через переменную
def str_iter():
    name = "Hello my first code".upper()  # создали строку новую с большой буквы
    n = 0  # счетчик итерации
    for i in name:
        print(i)
        n += 1  # увеличиваем счетчик
        print(n)


# использование нумерования авто
def str_enum():
    name = "Hello my first code".upper()
    # создали строку новую с большой буквы
    for n, i in enumerate(name):
        print(i)
        print(n)


# работа со списком
def work_with_list():
    list_numbers = [1, 2, 3, 4, 5]
    print(list_numbers, 'list 1')
    list_numbers2 = [1, 'Hi', [2, 3], 5]
    print(list_numbers2, 'list2')
    list_numbers2[3] = 'Test'
    print(list_numbers2, 'list 2 ch')
    list_numbers2.append('Test2')
    print(list_numbers2, 'list append')


# поиск в имени списка
def my_list_for():
    names = ["Иван", "Мария", "Владимир", "Сергей", "Николай"]
    friend_name = input('Введите имя: \n')
    # перебираем имя из списка
    for name in names:
        # сравниваем выбранное имя с имене который ввел пользователь
        if friend_name == name:
            print(f"Имя {friend_name} найдено")  # выводим результат


# ищем есть ли указанное имя в списке, это быстрее чем перебор
def search_friend_name():
    names = ["Иван", "Мария", "Владимир", "Сергей", "Николай"]
    name = input('Введите имя: \n')
    name = name.title()
    if name in names:
        # ищем вхождение в список, для проверки 1 букву имени делаем большой
        # выводим результат, но вывод все равно маленький,
        # так как строка не изменемый объект
        print(f"Имя {name} найдено!")
    else:
        print(f'Имя {name} не найдено')


# смена мест переменных в списке
def play_list_sorted():
    play_list = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5']
    print(play_list, 'Изначальный')
    # производим переприсваивание по индексу
    # s1 = play_list[1]
    # s2 = play_list[3]
    # но это запись очень длинная
    # play_list[1] = s2
    # play_list[3] = s1
    # множественное присваивание
    # play_list[1], play_list[3] = s2, s1
    # print(play_list, 'Измененный')
    # можно напрямую делать присваиваивание индексами
    play_list[1], play_list[3] = play_list[3], play_list[1]
    # тут создается картеж и менется местами занчения
    print(play_list)

# работа со словарем
def dict_list():
    contacts = {'Petya': 12345678, 'Lena': 987456321, 'Andru': 95175325}
    print(contacts, 'чистый список')
    # заменить значение ключа
    contacts['Petya'] = 10101010101
    print(contacts, 'заменили значении Пети')
    # добавим новый ключ
    contacts['John'] = 987654321
    print(contacts, 'добавили новый ключ/знач.')
    # если вызвать значение которого нет, будет ошибка
    # чтобы ее небыло воспользуемся меодом get
    print(contacts.get('Dasha'))
    print(contacts.get('Dasha', "Error"))  # error будет вместо None


dict_list()