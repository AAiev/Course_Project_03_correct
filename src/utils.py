import json
from operator import itemgetter


def create_dict_from_json(path):
    """
   create_dict_from_json(path) - переводит файл JSON в список словарей
   :param path: путь к файлу
   :return: список словарей
   """
    with open(path, "r", encoding="utf-8") as file:
        dict_operation = json.loads(file.read())
        return dict_operation


def five_last_successful_operations(list_operation):
    """
    five_last_successful_operations - Берет исходный список словарей,
    сортирует его по убыванию даты и выводит первые 5 операций успешно выполненных
    :return: list_last_five_operation - список из 5 последних операций
    """
    list_correct = [i for i in list_operation if 'date' in list(i.keys())]
    list_operation_sort_date = sorted(list_correct, key=itemgetter('date'), reverse=True)
    list_last_five_operation = []
    for operation in list_operation_sort_date:
        if len(list_last_five_operation) < 5:
            if operation['state'] == 'EXECUTED':
                list_last_five_operation.append(operation)
        else:
            break
    return list_last_five_operation
