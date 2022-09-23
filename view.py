from datetime import datetime as dt

from model import Contact
from log import add_log, get_log


def create_contact():
    print('введите данные нового контакта')
    name, surname, cell_number = input('Imya'), input('Fam'), input('введите номер телефона')

    new_contact = Contact()
    new_contact.name = name
    new_contact.surname = surname
    new_contact.cell_number = cell_number

    data_contact = new_contact.get_contact_value()
    # logging data
    add_log(data_contact)
    # Write data
    with open('contact_db.txt', 'a+', encoding='utf-8') as db:
        db.write(f'{" ".join(data_contact)}\n')


def print_data():
    pass


def get_contact():
    pass

def mode(select):
    flag = True
    while flag:
        if select == '1':
            create_contact()
            flag = False
        elif select == '2':
            create_contact()
            flag = False
        elif select == '3':
            create_contact()
            flag = False
        elif select == '4':
            create_contact()
            flag = False
        else:
            print('такой команды нет, выбирите команду от 1 до 4')

def start():
    print('---------------Телефонный справочник---------------')
    print('Программа может: \n1) Добавлять новые контакты\n2) Выгружать контакты в формате txt, json, csv, xlsx\n3) Импорт контактов из txt, json, csv, xlsx')
    select_mode = input('Что вы желате сделать (1 добавить / 2 выгрузить / 3 загрузить / 4 посмотреть логи)? ввод: ')
    mode(select_mode)



