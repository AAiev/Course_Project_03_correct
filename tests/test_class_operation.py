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