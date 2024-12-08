class Token:
    def __init__(self, typ, value):
        self.typ = typ
        self.value = value

    def __repr__(self):
        return f"Token({self.typ!r}, {self.value!r})"