import pytest
from src import *
from src.utils import data_sort_by_date, format_date, mask_amount_number, invoice_from, filter_list_execut


def test_data_for_sort():
    assert filter_list_execut([{'state': 'EXECUTED'}]) == [{'state': 'EXECUTED'}]
    assert format_date([{"date": "2019-08-26T10:50:58.294041"}]) == ['26-08-2019']
    assert data_sort_by_date([{"date": "2019-08-26T10:50:58.294041"}]) == [{"date": "2019-08-26T10:50:58.294041"}]
    assert mask_amount_number([{"to": "Счет 64686473678894779589"}]) == ['9589']
    assert (invoice_from([{"description": "Перевод организации", "from": "Maestro 1596837868705199"}]) ==
            ['Maestro 1596 83** **** 5199'])
