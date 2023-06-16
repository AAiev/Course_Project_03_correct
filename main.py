import os
from src.class_operation import Operation
from src.utils import create_dict_from_json, five_last_successful_operations

PATH_TO_OPERATIONS = os.path.join("data", "operations.json")


def main():

    # Конвертируем файл JSON в список PYTHON
    dict_from_json = create_dict_from_json(PATH_TO_OPERATIONS)

    # Получаем последние 5 успешных операций
    last_five_operation_list = five_last_successful_operations(dict_from_json)

    # Запускаем цикл по пследним 5 операциям и выводим на экран необходимую инфу.
    for operation_dict in last_five_operation_list:
        operation = Operation(operation_dict)
        print(operation.date_operation(), operation.title_operation())
        print(f'{operation.meaning_from()}{operation.meaning_to()}')
        print(f"{operation.amount_operation()}\n")


if __name__ == "__main__":
    main()
