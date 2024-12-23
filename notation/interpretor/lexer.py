from .token import Token
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Некорректный символ')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('INTEGER', int(result))

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()
            if self.current_char in '+-':
                token = Token('PLUS' if self.current_char == '+' else 'MINUS', self.current_char)
                self.advance()
                return token
            if self.current_char in '*/':
                token = Token('MULTIPLY' if self.current_char == '*' else 'DIVIDE', self.current_char)
                self.advance()
                return token
            self.error()
        return Token('EOF', None)