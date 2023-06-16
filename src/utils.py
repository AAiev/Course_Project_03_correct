import json


def create_dict_from_json(path):
    """
   create_dict_from_json(path) - переводит файл JSON в список словарей
   :param path: путь к файлу
   :return: список словарей
   """
    with open(path, "r", encoding="utf-8") as file:
        dict_operation = json.loads(file.read())
        return dict_operation
