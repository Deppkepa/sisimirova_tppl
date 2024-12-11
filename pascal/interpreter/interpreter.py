from .parser import Parser
from .AST import BinOp, Number

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
                var_name = node.left
                value = self.visit(node.right)
                self.variables[var_name] = value
                return value

    def visit(self, node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)

    def eval(self, program: str):
        self._parser.eval(program)
        for var in self.variables:
            self.normal_vars[var.value]=self.variables[var]
        return self.normal_vars
