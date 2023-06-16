class Operation:
    def __init__(self, dict_operation):
        self.dict_operation = dict_operation if dict_operation else {}

    def __repr__(self):
        return f"Operation(dict_operation={self.dict_operation})"

    def date_operation(self):
        """
        возвращает дату в формате: ДД.ММ.ГГГГ
        :return: дата в формате ДД.ММ.ГГГГ
        """
        date_operation_year = self.dict_operation['date'][0:4]
        date_operation_month = self.dict_operation['date'][5:7]
        date_operation_day = self.dict_operation['date'][8:10]
        return f'{date_operation_day}.{date_operation_month}.{date_operation_year}'

    def title_operation(self):
        """
        возвращает название операции
        """
        return self.dict_operation['description']
