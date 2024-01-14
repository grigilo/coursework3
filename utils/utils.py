import json
import os


def open_file():
    """Открываем файл json
    :param filename:
    :return:
    """
    # path = 'operations.json'
    # with open(path, encoding='utf-8') as file:
    #     new_data = json.loads(file.read())
    # return new_data

    json_file = os.path.join('..', '..', 'coursework3', 'operations.json')
    with open(json_file, encoding='utf-8') as file:
        new_data = json.loads(file.read())
    return new_data


print(open_file())


def filter_list_execut(data):
    """формируем новый список где state = EXECUTED

    :return:
    """
    new_data = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            new_data.append(item)
    return new_data


def modify_date(date):  # дата строкой
    """Фjрматирует дату

    :return:
    """
    return datetime


def modify_bill(bill):  # отправитель или получатель строкой
    """
    Форматируем реквизиты отправителя или получателя
    :param item_from:
    :return:
    """
    return


def format_operations(transaction):
    transaction['date'] = modify_date(transaction['date'])
    # обработка есть или нет ключ from
    transaction['from'] = modify_bill(transaction['from'])
    transaction['to'] = modify_bill(transaction['to'])

    return f"{transaction['date']}, \n"
