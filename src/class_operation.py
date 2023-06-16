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

    def meaning_from(self):
        """
        возвращает поле ОТКУДА в отформатированном варианте
        """
        if 'from' in self.dict_operation:
            title_from = self.dict_operation['from']
            digit_str = []
            sum_digit_in_str = sum(1 for i in title_from if i.isdigit())
            for i in title_from:
                if i.isdigit():
                    if len(digit_str) > 6 and (len(digit_str) < (sum_digit_in_str - 4 + digit_str.count(' '))):
                        digit_str.append('*')
                        if len(digit_str) % 4 == (0 + digit_str.count(' ')) and len(digit_str) > 0:
                            digit_str.append(' ')
                    else:
                        digit_str.append(i)
                        if len(digit_str) % 4 == (0 + digit_str.count(' ')) and 0 < len(digit_str) < sum_digit_in_str:
                            digit_str.append(' ')

            str_not_digit = ''.join([i for i in self.dict_operation['from'] if not i.isdigit()])
            if 'счет' in title_from.lower():
                return f"{str_not_digit}{''.join(digit_str[-7:]).replace(' ', '')} -> "
            else:
                return f"{str_not_digit}{''.join(digit_str[0:])} -> "

        else:
            return ""
