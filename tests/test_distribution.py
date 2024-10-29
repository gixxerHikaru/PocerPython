import re

from pocer.distribution import func
# テスト使い方
# 全通し pytest test_distribution.py
# クラス実行 pytest test_distribution.py::TestDistribution

# Suit Check
class TestSuitCheck:
    def test_one(self):
        pattern = r"[HCDS]"
        assert re.match(pattern, func()[0])

    def test_second(self):
        pattern = r"[HCDS]"
        assert re.match(pattern, func()[1])

    def test_third(self):
        pattern = r"[HCDS]"
        assert re.match(pattern, func()[2])

    def test_fourth(self):
        pattern = r"[HCDS]"
        assert re.match(pattern, func()[3])

    def test_fifth(self):
        pattern = r"[HCDS]"
        assert re.match(pattern, func()[4])

# Number Check
class TestNumberCheck:
    def test_one(self):
        for i in range(50):
            pattern = r".[2345678910JQKA]"
            assert re.match(pattern, func()[0])

    def test_second(self):
        for i in range(50):
            pattern = r".[2345678910JQKA]"
            assert re.match(pattern, func()[1])

    def test_third(self):
        for i in range(50):
            pattern = r".[2345678910JQKA]"
            assert re.match(pattern, func()[2])

    def test_fourth(self):
        for i in range(50):
            pattern = r".[2345678910JQKA]"
            assert re.match(pattern, func()[3])

    def test_fifth(self):
        for i in range(50):
            pattern = r".[2345678910JQKA]"
            assert re.match(pattern, func()[4])

# Not Same Check
class TestNotSame:
    def test_not_same(self):
        assert func()[0] != func()[1] != func()[2] != func()[3] != func()[4]

    def test_not_same_loop(self):
        for i in range(300):
            assert func()[0] != func()[1] != func()[2] != func()[3] != func()[4]

# Not Empty
class TestNotEmpty:
    def test_not_empty(self):
        assert func()[0] != func()[1] != func()[2] != func()[3] != func()[4] != ""
