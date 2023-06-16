from src.class_operation import Operation
test_dict_operation = {'date': '2019-12-08T22:46:21.935582',
                       'description': 'Открытие вклада',
                       'id': 863064926,
                       'operationAmount': {'amount': '41096.24',
                                           'currency': {'code': 'USD', 'name': 'USD'}},
                       'state': 'EXECUTED',
                       'to': 'Счет 90424923579946435907'}
test_dict_operation_2 = {'date': '2019-12-07T06:17:14.634890',
                         'description': 'Перевод организации',
                         'from': 'Visa Classic 2842878893689012',
                         'id': 114832369,
                         'operationAmount': {'amount': '48150.39',
                                             'currency': {'code': 'USD', 'name': 'USD'}},
                         'state': 'EXECUTED',
                         'to': 'Счет 35158586384610753655'}

test_dict_operation_3 = {'date': '2019-12-07T06:17:14.634890',
                         'description': 'Перевод организации',
                         'from': 'Счет 35158586384610753655',
                         'id': 114832369,
                         'operationAmount': {'amount': '48150.39',
                                             'currency': {'code': 'USD', 'name': 'USD'}},
                         'state': 'EXECUTED',
                         'to': 'Счет '}

test_operation = Operation(test_dict_operation)
test_operation_2 = Operation(test_dict_operation_2)
test_operation_3 = Operation(test_dict_operation_3)


def test_date_operation():
    """
    тест для функции date_operation - возвращает дату в заданном формате
    """
    assert test_operation.date_operation() == '08.12.2019'
    assert test_operation_2.date_operation() == '07.12.2019'


def test_title_operation():
    """
    тест для функции title_operation - возвращает название операции
    """
    assert test_operation.title_operation() == 'Открытие вклада'
    assert test_operation_2.title_operation() == 'Перевод организации'


def test_meaning_from():
    """
    тест для функции meaning_from - возвращает поле откуда, если имеется
    """
    assert test_operation.meaning_from() == ''
    assert test_operation_2.meaning_from() == 'Visa Classic 2842 87** **** 9012 -> '
    assert test_operation_3.meaning_from() == 'Счет **3655 -> '


def test_meaning_to():
    """
    тест для функции meaning_to - возвращает поле куда
    """
    assert test_operation.meaning_to() == 'Счет **5907'
    assert test_operation_2.meaning_to() == 'Счет **3655'
    assert test_operation_3.meaning_to() == 'Счет '


def test_amount_operation():
    """
    тест для функции amount_operation - возвращает сумму и валюту операции
    """
    assert test_operation.amount_operation() == '41096.24 USD'
