# 1 - создать водителя и машину, удалить, посмотреть машины, усложнение задания
# разработать возможность загрузки и сохранения данных чтобы файлы сохранялись
def func():
    driver = {'Петя': 'BMW', 'Лена': 'AUDI', 'Андрюха': 'MAZDA'}
    print(driver)


# 2 - Список дел - добавить, посмотреть, удалить, изменить. (методы для списков)
def to_do_list():
    to_do = []
    while True:
        do = input('Задание:\n1 добавить\n2 Посмотреть\n3 удалить\n4 изменить\nЧто будем делать?\n')
        if do == '1':
            one = input('что добавляем?\n')
            if one != '':
                to_do.append(one)
            else:
                print('Данные введены некоректно!')
        elif do == '2':
            print(f'Список дел: {to_do}')
        elif do == '3':
            try:
                print(to_do)
                three = input('Введите что удалить\n')
                to_do.remove(three)
                print(f'Дело -> {three} удалено')
            except ValueError:
                print(f'Таких данных нет')
        elif do == '4':
            try:
                print(to_do)
                four = input('Введите что изменить\n')
                idx = to_do.index(four)
                to_do.remove(four)
                n_four = input('Введите на что изменить\n')
                to_do.insert(idx, n_four)
                print(to_do)
            except ValueError:
                print(f'Введены некоректные данные!')
        elif do == 'стоп':
            break


# 3 - изменить логику программы, чтобы менять порядок песен не по индексу а по имени элемента
def play_list_sorted():
    play_list = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5']
    print(play_list, 'Изначальный')
    answer = input('Введите что изменить\n')
    idx = play_list.index(answer)
    answer_2 = input('Введите на что изменить\n')
    idx_2 = play_list.index(answer_2)
    play_list[idx], play_list[idx_2] = play_list[idx_2], play_list[idx]
    print(play_list)
