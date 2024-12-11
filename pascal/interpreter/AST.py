from .token import Token
class Node:
    pass

class Number(Node):
    def __init__(self, token: Token):
        self.token = token

class BinOp(Node):
    def __init__(self, left: Node, op:Token, right:Node):
        self.left = left
        self.op = op
        self.right = right
