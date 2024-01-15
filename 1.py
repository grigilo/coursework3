import re

x = [
    {'id': 863064926,
     'state': 'EXECUTED',
     'date': '2019-12-08T22:46:21.935582',
     'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Открытие вклада',
     'to': 'Счет 90424923579946435907'}, {'id': 114832369,

                                          'state': 'EXECUTED',
                                          'date': '2019-12-07T06:17:14.634890',
                                          'operationAmount': {'amount': '48150.39',
                                                              'currency': {'name': 'USD', 'code': 'USD'}},
                                          'description': 'Перевод организации',
                                          'from': 'Visa Classic 2842878893689012',
                                          'to': 'Счет 35158586384610753655'},

    {'id': 154927927,
     'state': 'EXECUTED',
     'date': '2019-11-19T09:22:25.899614',
     'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод организации',
     'from': 'Maestro 7810846596785568',
     'to': 'Счет 43241152692663622869'},

    {'id': 482520625,
     'state': 'EXECUTED',
     'date': '2019-11-13T17:38:04.800051',
     'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод со счета на счет',
     'from': 'Счет 38611439522855669794',
     'to': 'Счет 46765464282437878125'},

    {'id': 801684332,
     'state': 'EXECUTED',
     'date': '2019-11-05T12:04:13.781725',
     'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Открытие вклада',
     'to': 'Счет 77613226829885488381'}]


# def mask_amount_number(x):
#     """
#     Маскировка счета to
#     :param amount_number:
#     :return:
#     """
#     amount_number_operations = []
#     for amount_number in x:
#         # format_to_chek = re.findall("....", amount_number["to"])
#         # print(format_to_chek)
#         # check_to_format = format_to_chek[4:]
#         # number_amount = check_to_format[0].replace(check_to_format[0], '**'), check_to_format[1]
#         # amount_mask = "".join(list(number_amount))
#         # amount_number_operations.append(amount_mask)
#         amount_number_operations.append(amount_number['to'][21:25])
#
#     return amount_number_operations


# y = mask_amount_number(x)
# print(y)
#
# w = 'Счет 77613226829885488381'
# print(w[21:25])


def invoice_from(x):
    """
    Скрываем реквезиты отправителя
    :param data:
    :param item_from:
    :return:
    """
    card_number_operation = []
    for item in x:
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


y = invoice_from(x)

print(y)
