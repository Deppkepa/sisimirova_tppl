class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Некорректный синтаксис')

    def parse(self):
        result = []
        while self.current_token.typ != 'EOF':
            if self.current_token.typ == 'INTEGER':
                for char in range(len(result)):
                    if result[0] in '+/*-':
                        result.insert(char, str(self.current_token.value))
                        break
                    elif result[char] in '+/*-' and  result[char - 1].isdigit() == True and char != len(result) - 1 and result[char + 1].isdigit() != True:
                        result.insert(char + 1, str(self.current_token.value))
                        break
                    elif len(self.lexer.text) == self.lexer.pos:
                        if result[len(result) - 1] in '+-*/' and result[len(result) - 2] in '+-*/':
                            continue
                        else:
                            result.append(str(self.current_token.value))
                            break
                    elif result[len(result)-1] in "+-/*" and len(result) == 2:
                        result.append(str(self.current_token.value))
                self.current_token = self.lexer.get_next_token()
            elif self.current_token.typ in ('PLUS', 'MINUS'):
                result.append(self.current_token.value)
                if self.lexer.text[self.lexer.pos - 3] in '+-/*':
                    for char in range(len(result)- 1, -1, -1):
                        if result[char] in '+-/*' and result[char - 1] in '+-/*':
                            op = result[char]
                            result[char] = result[char - 1]
                            result[char - 1] = op
                            break
                self.current_token = self.lexer.get_next_token()
            elif self.current_token.typ in ('MULTIPLY', 'DIVIDE'):
                result.append(self.current_token.value)
                self.current_token = self.lexer.get_next_token()
        if result[len(result) - 1] in '-':
            op = result[len(result) - 1]
            result = result[:len(result) - 1]
            result.insert(0, op)
        return ' '.join(helper(result))


def helper(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    max_precedence = -1
    main_operator_index = -1
    for i in range(len(expr)):
        if expr[i] in precedence:
            if precedence[expr[i]] > max_precedence:
                max_precedence = precedence[expr[i]]
                main_operator_index = i
    if main_operator_index == -1:
        return expr
    left_expr = helper(expr[:main_operator_index])
    right_expr = helper(expr[main_operator_index + 1:])
    return ['('] + left_expr + [expr[main_operator_index]] + right_expr + [')']
