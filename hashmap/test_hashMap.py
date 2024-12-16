import pytest
from hashMap import SpecialHashMap

class TestHashMap:
    def test_create_value_1(self):
        map_my = SpecialHashMap()
        map_my["value1"] = 1
        map_my["value2"] = 2
        map_my["value3"] = 3
        map_my["1"] = 10
        map_my["2"] = 20
        map_my["3"] = 30
        map_my["1, 5"] = 100
        map_my["5, 5"] = 200
        map_my["10, 5"] = 300
        assert map_my["value1"] == 1
        assert map_my["value2"] == 2
        assert map_my["value3"] == 3
        assert map_my["1"] == 10
        assert map_my["2"] == 20
        assert map_my["3"] == 30
        assert map_my["1, 5"] == 100
        assert map_my["5, 5"] == 200
        assert map_my["10, 5"] == 300

    def test_iloc(self):
        map_my = SpecialHashMap()
        map_my["value1"] = 1
        map_my["value2"] = 2
        map_my["value3"] = 3
        map_my["1"] = 10
        map_my["2"] = 20
        map_my["3"] = 30
        map_my["1, 5"] = 100
        map_my["5, 5"] = 200
        map_my["10, 5"] = 300
        assert map_my.iloc[0] == 10
        assert map_my.iloc[2] == 300
        assert map_my.iloc[5] == 200
        assert map_my.iloc[8] == 3
    def test_create_value_2(self):
        map_my = SpecialHashMap()
        map_my["value1"] = 1
        map_my["value2"] = 2
        map_my["value3"] = 3
        map_my["1"] = 10
        map_my["2"] = 20
        map_my["3"] = 30
        map_my["(1, 5)"] = 100
        map_my["(5, 5)"] = 200
        map_my["(10, 5)"] = 300
        map_my["(1, 5, 3)"] = 400
        map_my["(5, 5, 4)"] = 500
        map_my["(10, 5, 5)"] = 600
        assert map_my["value1"] == 1
        assert map_my["value2"] == 2
        assert map_my["value3"] == 3
        assert map_my["1"] == 10
        assert map_my["2"] == 20
        assert map_my["3"] == 30
        assert map_my["(1, 5)"] == 100
        assert map_my["(5, 5)"] == 200
        assert map_my["(10, 5)"] == 300
        assert map_my["(1, 5, 3)"] == 400
        assert map_my["(5, 5, 4)"] == 500
        assert map_my["(10, 5, 5)"] == 600

    def test_ploc(self):
        map_my = SpecialHashMap()
        map_my["value1"] = 1
        map_my["value2"] = 2
        map_my["value3"] = 3
        map_my["1"] = 10
        map_my["2"] = 20
        map_my["3"] = 30
        map_my["(1, 5)"] = 100
        map_my["(5, 5)"] = 200
        map_my["(10, 5)"] = 300
        map_my["(1, 5, 3)"] = 400
        map_my["(5, 5, 4)"] = 500
        map_my["(10, 5, 5)"] = 600
        assert map_my.ploc(">=1") == {'1': 10, '2': 20, '3': 30}
        assert map_my.ploc("<3") == {'1': 10, '2': 20}
        assert map_my.ploc(">0, >0") == {'(1, 5)': 100, '(5, 5)': 200, '(10, 5)': 300}
        assert map_my.ploc(">=10, >0") == {'(10, 5)': 300}
        assert map_my.ploc("<5, >=5, >=3") == {'(1, 5, 3)': 400}
        assert map_my.ploc("<>5") == {'1': 10, '2': 20, '3': 30}
        with pytest.raises(SyntaxError, match="Неправильно задано количество условий. Совпадения не найдены"):
            map_my.ploc("<5, =3")
        with pytest.raises(SyntaxError, match="Неправильно задано количество условий. Совпадения не найдены"):
            map_my.ploc("<=5, >5, >5")

        with pytest.raises(SyntaxError, match="Неправильно задано количество условий. Совпадения не найдены"):
            map_my.ploc("<>5, <>5, <>5")






