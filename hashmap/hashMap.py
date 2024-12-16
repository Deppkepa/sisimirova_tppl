import re

class SpecialHashMap:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    @property
    def iloc(self):
        sorted_keys = sorted(self.data.keys())
        values = [self.data[key] for key in sorted_keys]
        return values
    def check_key_char(self, key):
        for char in key:
            if char.isalpha():
                return True
        return False
    def ploc(self, condition):
        parts = re.split(r'[<>=,]+', condition.replace(" ", ""))
        operators = re.findall(r'[<>=]+', condition.replace(" ", ""))
        parts = list(filter(None, parts))
        results = {}
        key_parts = []
        for key, value in self.data.items():
            cleaned_key = re.sub(r'[()]', '', key).split(',')
            if self.check_key_char(cleaned_key[0]):
                continue
            key_parts = list(map(float, cleaned_key))
            if len(key_parts) != len(parts):
                continue

            match = True
            for i in range(len(parts)):
                number = key_parts[i]
                op = operators[i] if i < len(operators) else ""

                if op == '<' and not (number < float(parts[i])):
                    match = False
                    break
                elif op == '<=' and not (number <= float(parts[i])):
                    match = False
                    break
                elif op == '>' and not (number > float(parts[i])):
                    match = False
                    break
                elif op == '>=' and not (number >= float(parts[i])):
                    match = False
                    break
                elif op == '=' and not (number == float(parts[i])):
                    match = False
                    break
                elif op == '<>' and not (number != float(parts[i])):
                    match = False
                    break

            if match:
                results[key] = value
        if len(results) == 0:
            raise SyntaxError("Неправильно задано количество условий. Совпадения не найдены")
        return results