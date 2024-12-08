import pytest
from interpretor import Interpeter
@pytest.fixture()
def interpreter():
    return Interpeter()

class TestInterpreter:
    def test_add(self, interpreter):
        assert interpreter.eval('+ - 13 4 55') == '( 13 - ( 4 + 55 ) )' # 13 - 4 + 55
        assert interpreter.eval('+ + 10 20 30') == '( 10 + ( 20 + 30 ) )' # 10 + 20 + 30
        assert interpreter.eval('- - 1 2') == '( - ( 1 - 2 ) )' # - 1 - 2
        assert interpreter.eval('+ 2 * 2 - 2 1') == '( ( 2 + 2 ) * ( 2 - 1 ) )' # 2 + 2 * ( 2 - 1 )
        assert interpreter.eval('/ + 3 10 * + 2 3 - 3 5') == '( ( 3 + 10 ) / ( ( 2 + 3 ) * ( 3 - 5 ) ) )' # ( 3 + 10 ) / ( 2 + 3 ) * ( 3 - 5 )
