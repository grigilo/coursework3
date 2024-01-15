from src.utils import open_file, filter_list_execut, data_sort_by_date, format_date, \
    invoice_from, mask_amount_number


data = open_file()
data_executed = filter_list_execut(data)
data_date = data_sort_by_date(data_executed)
date = format_date(data_date)
hide_invoice_from = invoice_from(data_date)
amount_number = mask_amount_number(data_date)


for item in range(len(data_date)):
    print(f'{date[item]} {data_date[item]["description"]}\n'
          f"{hide_invoice_from[item]} => Счёт: **{amount_number[item]}")
    print(f'{data_date[item]["operationAmount"]["amount"]} {data_date[item]["operationAmount"]["currency"]["name"]}\n')
