from .parser import Parser
from .AST import BinOp, Number#, Variable#, UnaryOp
class Interpreter:
    def __init__(self):
        self._parser = Parser(self)
        self.variables = dict()
        self.normal_vars = dict()

    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)

    def _visit_binop(self, node: BinOp):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)

            case "-":
                return self.visit(node.left) - self.visit(node.right)

            case "/":
                return self.visit(node.left) / self.visit(node.right)

            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case ":=":
                # Здесь предполагаем, что node.left - это идентификатор переменной,
                # а node.right - значение, которое нужно присвоить.
                var_name = node.left  # Получаем имя переменной
                value = self.visit(node.right)  # Вычисляем значение для присвоения
                # Затем здесь нужно сохранить значение в области видимости
                self.variables[var_name] = value  # Сохраняем значение в словаре
                return value  # Можно вернуть присвоенное значение, если это необходимо



            #case _:
            #    raise NotImplementedError("Unknown operation")
                # raise RuntimeError("Invalid operator")
    def visit(self, node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        #elif isinstance(node, UnaryOp):
        #    return self._visit_unary(node)
        #elif isinstance(node, Variable):
        #    return self._visit_binop(node)


    #def _visit_unary(self, node):
    #    match node.op.value:
    #        case "+":
    #            return +self.visit(node.expr)
    #        case "-":
    #            return +self.visit(node.expr)
    #        case _:
    #            raise RuntimeError("Bad UnaryOp")
    def eval(self, program: str):
        #trees = self._parser.eval(program)
        #for tree in trees:
        #    self.visit(tree)
        self._parser.eval(program)
        for var in self.variables:
            self.normal_vars[var.value]=self.variables[var]
        return self.normal_vars
