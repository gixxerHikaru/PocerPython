from pocer.conversion import func
# テスト使い方
# 全通し pytest test_app.py
# クラス実行 pytest test_app.py::TestHighCard


# High Card
class TestHighCard:
    def test(self):
        answer = 1
        assert "High Card" == func(answer)

# A Pair
class TestAPair:
    def test(self):
        answer = 2
        assert "A Pair" == func(answer)

# Two Pair
class TestTwoPair:
    def test(self):
        answer = 3
        assert "Two Pair" == func(answer)

# Three Of A Kind
class TestThreeOfAKind:
    def test(self):
        answer = 4
        assert "Three Of A Kind" == func(answer)

# Straight
class TestStraight:
    def test(self):
        answer = 5
        assert "Straight" == func(answer)

# flush
class TestFlush:
    def test(self):
        answer = 6
        assert "Flush" == func(answer)

#  A Full Housh
class TestFullHouse:
    def test(self):
        answer = 7
        assert "A Full House" == func(answer)

# Four Of A Kind
class TestFourOfKind:
    def test(self):
        answer = 8
        assert "Four Of A Kind" == func(answer)

# Straight Flush
class TestStraightFlush:
    def test(self):
        answer = 9
        assert "Straight Flush" == func(answer)

# Royal flush
class TestRoyalFlush:
    def test(self):
        answer = 10
        assert "Royal Flush" == func(answer)
# Other
class TestOther:
    def test(self):
        answer = 0
        assert None == func(answer)
           