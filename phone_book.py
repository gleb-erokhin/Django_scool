# дз - написать 4 пункт изменение телефонных номеров
def phone_book():
    contacts = {'Petya': 12345678, 'Lena': 987456321, 'Andru': 95175325}
    while True:
        command = input("1 - Добавить\n2 - удалить\n3 - Просмотр\n4 - Изменить номер\nВведите команду:\n")
        if command == '1':
            name = input('Введите имя:\n')
            if contacts.get(name):  # проверяем есть ли введенное имя в списке контактов
                # если такого имени нет, то в условии будет None, а это значит Ложь
                print('Такое имя существует!')  # печатаем ошибку
                continue  # возврат в цикл
            tel = int(input('Введите телефон:\n'))
            contacts[name] = tel
        elif command == '2':  # функция удаления контакта
            name = input('Введите имя:\n')
            if contacts.get(name):
                contacts.pop(name)
                print(f'Контакт {name} удален')
            else:
                print(f'Имя {name} не найдено')
        elif command == '3':
            # функция просмотра словаря ключ / знач.
            # for name in contacts:  # проход по всему словарю
            #     print(name, contacts[name])  # выводим пару клю / знач.
            # сделаем вывод проще и красивее
            for name, phone in contacts.items():
                print(f'{name} - {phone}')
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ДЗ
        elif command == '4':
            name = input('Введите имя:\n')
            if contacts.get(name):
                tel = input('Введите телефон:\n')
                contacts.update({name: tel})
                print(f'Контакт {name} изменен')
                print(f'Данные {contacts} обновлены')
            else:
                print(f'Имя {name} не найдено')


phone_book()
