# 1 - создать водителя и машину, удалить, посмотреть машины, усложнение задания
# разработать возможность загрузки и сохранения данных чтобы файлы сохранялись
def drv_stand():
    car_driver = {'Петя': 'BMW', 'Лена': 'AUDI', 'Андрюха': 'MAZDA'}
    # print(car_driver)
    while True:
        print('Введите информацию о машине и водителе')
        add_inf = input('1 добавить, 2 изменить, 3 посмотреть, 4 удалить\n')
        if add_inf == '1':
            driver = input('Введите имя водителя: ')
            car = input('Введите марку машины: ')
            car_driver.setdefault(driver, car)
            # print(car_driver)
        elif add_inf == '2':  # возможность изменения только машины и только водителя
            up_drv = input('Введите имя водителя: ')
            up_car = input('введите новое имя машины: ')
            car_driver.update({up_drv: up_car})
        elif add_inf == '3':
            print(car_driver)
        elif add_inf == '4':
            del_drv = input('Введите имя водителя для удаления: ')
            car_driver.pop(del_drv)
        elif add_inf == 'стоп' or 'stop':
            break


# 2 - Список дел - добавить, посмотреть, удалить, изменить. (методы для списков)
def to_do_list():
    to_do = []
    while True:
        command = input('Задание:\n1 добавить\n2 Удалить\n3 Посмотреть\n4 изменить\nЧто будем делать?\n')
        if command == '1':
            task = input('что добавляем?\n')
            if task != '':
                to_do.append(task)
            else:
                print('Данные введены некоректно!')
        elif command == '2':
            try:
                for i, task in enumerate(to_do):
                    print(f'# {i + 1}: {task}')
                task_number = int(input('Введите номер задачи\n'))
                task = to_do.pop(task_number)
                print(f"Задача -> '{task}' удалено")
            except ValueError:
                print(f'Таких данных нет')
            except TypeError:
                print('Нечего удалять')
                continue
        elif command == '3':
            for i, task in enumerate(to_do):
                print(f'# {i + 1}: {task}')
        elif command == '4':
            try:
                task_number = int(input('Введите номер задачи\n'))
                task = input('Введите задачу\n')
                to_do[task_number] = task
                # idx = to_do.index(task_number)
                # to_do.remove(idx)
                # task = input('Введите задачу\n')
                # to_do.insert(idx, task)
                #
            except ValueError:
                print(f'Введены некоректные данные!')
        elif command == 'стоп':
            break


to_do_list()

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


# 1a возможность открытия данных из файла и сего сохранение
def drv_stand_new():
    open_list = open('car_driver.txt', encoding='UTF-8')  # открываем файл внешний
    car_driver = open_list.read()  # переводим чтение файла в переменную
    open_list.close()
    while True:
        print('Введите информацию о машине и водителе')
        add_inf = input('1 добавить, 2 изменить, 3 посмотреть, 4 удалить\n')
        if add_inf == '1':
            driver = input('Введите имя водителя: ')
            car = input('Введите марку машины: ')
            with open('car_driver.txt', 'a', encoding='UTF-8') as f:
                f.writelines(driver)
                f.writelines(car)
            # print(car_driver)
        elif add_inf == '2':  # возможность изменения только машины и только водителя
            up_drv = input('Введите имя водителя: ')
            up_car = input('введите новое имя машины: ')
            car_driver.update({up_drv: up_car})
        elif add_inf == '3':
            print(car_driver)
        elif add_inf == '4':
            del_drv = input('Введите имя водителя для удаления: ')
            car_driver.pop(del_drv)
        elif add_inf == 'стоп' or 'stop':
            break



def open_write():
    # with open('test.txt', encoding='UTF-8') as f: # открываем файл внешний
    #     f.read()  # переводим чтение файла в переменную
    #     f.close()
    #     print(f, 'open, file is empty')
    with open('test.txt', 'a+', encoding='UTF-8') as f:
        f.write('test5')
        print(f, 'open, write file')
    open_list = open('test.txt', encoding='UTF-8')  # открываем файл внешний
    car_driver = open_list.read()  # переводим чтение файла в переменную
    open_list.close()
    print(car_driver)



