from utils.utils import open_file, get_format_date_executed_transactions, filter_list_execut, format_operations

data = open_file() #Все операции
data = filter_list_execut(data) # Только EXECUTED
data = data.sort()[0:5] # [start:stop:step] сортировка по дате и срез 5 операций

for trans in data:
    formatted = format_operations(trans)
    print(formatted)

print(open_file())
