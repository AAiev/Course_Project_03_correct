class Operation:
    def __init__(self, dict_operation):
        self.dict_operation = dict_operation if dict_operation else {}

    def __repr__(self):
        return f"Operation(dict_operation={self.dict_operation})"
