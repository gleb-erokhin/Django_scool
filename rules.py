# правило множественного присваивания
def set_func():
    my_list = [1, 2, 3, 4]
    # множественно присваиваем переменные значениям в спсике
    a, b, c, d = my_list
    print(a, b, c, d)

    my_list_2 = [5, 6, 7, 8]
    # знак * присваивает последнии 2 значения в 1 перменную
    a, b, *c, = my_list_2
    print(a, b, c)

    my_list_3 = [5, 6, 7, 8, 9]
    # но новая переменная добавиться дальше
    a, b, *c, d = my_list_3
    print(a, b, c, d)


# картежи, не изменны, заменить добавить данные невозожно
def tuple_list():
    list_numbers = (1, 2, 3, 4, 5)  # картеж
    print(list_numbers)

    list_numbers = (1, 'Hi', [3, 4], 5)  # картеж
    print(list_numbers)

tuple_list()