import pytest
from interpreter import Interpreter
def interpreter():
    return Interpreter()

class TestInterpreter:
    def test_add(self):
        assert interpreter().eval("""
BEGIN
x:=2+2  
END""") == {"x": 4.0}



    def test_sub(self):
        assert interpreter().eval("""BEGIN 
x:=2-2 
END""") == {"x": 0.0}

        assert interpreter().eval("""BEGIN 
x:=2-3 
END""") == {"x": -1.0}

    def test_spaces(self):
        assert interpreter().eval("""BEGIN 
x               :=                    2      +         2 
END""") == {"x": 4.0}

    def test_int(self):
        assert interpreter().eval("""BEGIN 
x:=222+12323232
END""") == {"x": 12323454.0}

    def test_float(self):
        assert interpreter().eval("""BEGIN 
x:=2.5+2.5
END""") == {"x": 5.0}

    def test_term(self):
        assert interpreter().eval("""BEGIN 
x:=2+2-2
END""") == {"x": 2.0}

    def test_term2(self):
        assert interpreter().eval("""BEGIN 
x:=2+2*2
END""") == {"x": 6.0}

    def test_term3(self):
        assert interpreter().eval("""BEGIN 
x:=2+2/2
END""") == {"x": 3.0}

    def test_term4(self):
        assert interpreter().eval("""BEGIN 
x:=2*2+2
END""") == {"x": 6.0}

    def test_paren(self):
        assert interpreter().eval("""BEGIN 
x:=(2+2)*2
END""") == {"x": 8.0}
    def test_paren2(self):
        assert interpreter().eval("""BEGIN 
x:=(((2.5+2.5)))
END""") == {"x": 5.0}
    def test_paren3(self):
        assert interpreter().eval("""BEGIN 
x:=2 + (2 * (3 + 5))
END""") == {"x": 18.0}
        assert interpreter().eval("""BEGIN
        x:=18;
        t:=x+3;
        x:=t;
END""") == {"t": 21.0, "x": 21.0}
    def test_error(self):
        with pytest.raises(SyntaxError, match="bad token"):
            interpreter().eval("""BEGIN
        x@:=1;
END""")
    def test_error2(self):
        with pytest.raises(SyntaxError):
            interpreter().eval("x:=0")
    def test_multiply(self):
        assert interpreter().eval("""BEGIN
        x:=2*2
END""") == {"x": 4.0}

