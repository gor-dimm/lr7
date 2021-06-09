#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 15. Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата рождения (список из
# трех чисел). Написать программу, выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть упорядочены по датам рождения; вывод на экран информации о людях,
# родившихся под знаком, название которого введено с клавиатуры; если таких нет, выдать на дисплей соответствующее
# сообщение.

import sys
import json

if __name__ == '__main__':
    # Список людей.
    peoples = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия и имя? ")
            zod = input("Знак Зодиака? ")
            birth = input("Дата рождения? ")
            # Создать словарь.
            people = {
            'name': name,
            'zod': zod,
            'birth': birth,
            }
            #Добавить словарь в список.
            peoples.append(people)
            # Отсортировать список в случае необходимости.
            if len(peoples) > 1:
                peoples.sort(key=lambda item: item.get('birth', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
            )
            print(line)
            print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Фамилия и имя",
            "Знак Зодиака",
            "Дата рождения" ))
            print(line)
            for idx, people in enumerate(peoples, 1):
                print('| {:>4} | {:<30} | {:<20} | {:>15} |'.format(idx,
                people.get('name', ''), people.get('zod', ''), people.get('birth', 0)))
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            sel = (parts[1])
            count = 0
            for people in peoples:
                if people.get('zod') == sel:
                    count += 1
                    print('{:>4}: {}'.format(count, people.get('name', '')))
                    if count == 0:
                       print("Люди с данным знаком Зодиака не найдены.")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                peoples = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(peoples, f, ensure_ascii=False)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <знак зодиака> - запросить людей с знаком Зодиака;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)