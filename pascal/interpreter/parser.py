from .lexer import Lexer
from .AST import BinOp, Number
from .token import TokenType

class Parser:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.assignment_is_here = False
        self._lexer = Lexer(self)
        self._current_token = None

    def separation_complex_statement(self, program):
        lines = program.strip().splitlines()
        if lines[0].startswith('BEGIN') != True or lines[-1].startswith('END') != True:
            raise SyntaxError("Не является программой Pascal(Нету 'BEGIN' или 'END')")
        expressions = []
        for line in lines:
            line = line.strip()
            if line.startswith("BEGIN") or line.startswith("END"):
                continue
            if line:
                expressions.append(line)
        return expressions

    def __term(self):
        result = self.__factor()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in ["*", "/"]:
                break
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.__factor())
        return result

    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        #else:
        #    raise SyntaxError("invalid token order")

    def __factor(self):
        token = self._current_token
        if token.type_ == TokenType.VARIABLE:
            var_token = token
            self.__check_token(TokenType.VARIABLE)
            op_token = self._current_token
            self.__check_token(TokenType.ASSIGNMENT)
            expr = self.__expr()
            return BinOp(var_token, op_token, expr)
        if token.type_ == TokenType.INTEGER_NUMBER:
            self.__check_token(TokenType.INTEGER_NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPAREN:
            self.__check_token(TokenType.LPAREN)
            result = self.__expr()
            self.__check_token(TokenType.RPAREN)
            return result
        #raise SyntaxError("Invalid factor")
        
    def __expr(self) -> BinOp:
        result = self.__term()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.__term())
        return result

    def eval(self, p: str):
        text = self.separation_complex_statement(p)
        for i in text:
            self._lexer.init(i)
            self._current_token = self._lexer.next()
            self.interpreter.visit(self.__expr())



