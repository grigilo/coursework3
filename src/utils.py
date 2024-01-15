import json
import os
from datetime import datetime
import re


def open_file():
    """Открываем файл json
    :return:
    """

    json_file = os.path.join('..', '..', 'coursework3', 'operations.json')
    with open(json_file, encoding='utf-8') as file:
        new_data = json.loads(file.read())
    return new_data


def filter_list_execut(data):
    """формируем новый список, где state = EXECUTED

    :return:
    """
    new_data = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            new_data.append(item)
    return new_data


def data_sort_by_date(data):
    """
    Сортируем список по дате
    и возвращаем последние 5 операции
    :param data:
    :return:
    """
    sorted_date = sorted(data, key=lambda x: x['date'], reverse=True)
    last_five = sorted_date[:5]
    return last_five


def format_date(data):
    """
    Отформатируем даты в нужный нам вид
    :param data:
    :return:
    """
    x = []
    for item in data:
        item = datetime.fromisoformat(item['date'].replace('T', ' '))
        x.append(item.strftime('%d-%m-%Y'))

    return x


def invoice_from(data):
    """
    Скрываем реквезиты отправителя
    :param data:
    :return:
    """
    card_number_operation = []
    for item in data:
        if item["description"] == "Открытие вклада":
            item['from'] = f'Пополнение счёта: {item["to"][5:]}'
        mask_card = item["from"].split()
        mask_card_copy = mask_card.copy()
        del mask_card_copy[-1]
        card_mask = re.findall("....", mask_card[-1])
        number_card = card_mask[0], card_mask[1][0:2] + '**', card_mask[2].replace(card_mask[2], "****"), card_mask[3:]
        mask_number = " ".join(number_card[3])
        card_number_operation.append(f"{' '.join(mask_card_copy)} {' '.join(list(number_card[0:3]))} {mask_number}")

    return card_number_operation


def mask_amount_number(amount_numbers):
    """
    Маскировка счета "to"
    :return:
    """
    amount_number_operations = []
    for amount_number in amount_numbers:
        amount_number_operations.append(amount_number['to'][21:25])

    return amount_number_operations
