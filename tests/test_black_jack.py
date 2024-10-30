from black_jack.black_jack import func
# テスト使い方
# 全通し pytest test_black_jack.py
# クラス実行 pytest test_black_jack.py::TestHighCard


# Black Jack
class TestBlackJack:
    def test_hh(self):
        cards = ['HA', 'H10']
        assert "Black Jack" == func(cards)

    def test_cc(self):
        cards = ['CA', 'C10']
        assert "Black Jack" == func(cards)

    def test_hc(self):
        cards = ['HA', 'C10']
        assert "Black Jack" == func(cards)

    def test_ds(self):
        cards = ['DA', 'S10']
        assert "Black Jack" == func(cards)        

# Lose
class TestLose:
    def test_22(self):
        cards = ['HK', 'H10', 'H2']
        assert "You Lose..." == func(cards)

    def test_23(self):
        cards = ['CA', 'C9', 'C4']
        assert "You Lose..." == func(cards)

    def test_24(self):
        cards = ['HA', 'C8', 'D5', 'SA']
        assert "You Lose..." == func(cards)

    def test_25(self):
        cards = ['D4', 'S10', 'HA']
        assert "You Lose..." == func(cards) 