from datetime import datetime as dt


def add_log(data):
    with open('log.txt', 'a+', encoding='utf-8') as file:
        time = dt.now()

        file.write(f'{" ".join(data)} {time}\n')


def get_log():
    with open('log.txt', 'r', encoding='utf-8') as file:
        data_set = [i for i in file]

    return data_set
