from pocer.judge import func
# テスト使い方
# 全通し pytest test_judge.py
# クラス実行 pytest test_judge.py::TestHighCard


# High Card
class TestHighCard:
    def test_high_card(self):
        cards = ['H2', 'D3', 'C4', 'S5', 'H7']
        assert "High Card" == func(cards)

# A Pair
class TestAPair:
    def test_1(self):
        cards = ['H2', 'D2', 'C4', 'S5', 'H7']
        assert "A Pair" == func(cards)

    def test_2(self):
        cards = ['H3', 'D3', 'C4', 'S5', 'H7']
        assert "A Pair" == func(cards)

    def test_a(self):
        cards = ['H2', 'D3', 'C4', 'SA', 'HA']
        assert "A Pair" == func(cards)

# Two Pair
class TestTwoPair:
    def test_1(self):
        cards = ['H2', 'D2', 'C4', 'S4', 'H7']
        assert "Two Pair" == func(cards)

    def test_2(self):
        cards = ['H3', 'D3', 'C5', 'S5', 'H7']
        assert "Two Pair" == func(cards)

    def test_a(self):
        cards = ['H2', 'D4', 'C4', 'SA', 'HA']
        assert "Two Pair" == func(cards)

# Three Of A Kind
class TestThreeOfAKind:
    def test_1(self):
        cards = ['H2', 'D2', 'C2', 'S5', 'H7']
        assert "Three Of A Kind" == func(cards)
    def test_2(self):
        cards = ['H3', 'D3', 'C3', 'S5', 'H7']
        assert "Three Of A Kind" == func(cards)
    def test_a(self):
        cards = ['H2', 'D4', 'CA', 'SA', 'HA']
        assert "Three Of A Kind" == func(cards)

# Straight
class TestStraight:
    def test_1(self):
        cards = ['H2', 'D3', 'C4', 'S5', 'H6']
        assert "Straight" == func(cards)

    def test_2(self):
        cards = ['H3', 'D4', 'C5', 'S6', 'H7']
        assert "Straight" == func(cards)

    def test_a(self):
        cards = ['H10', 'DJ', 'CQ', 'SK', 'HA']
        assert "Straight" == func(cards)

# flush
class TestFlush:
    def test_h(self):
        cards = ['H2', 'H3', 'H4', 'H5', 'H7']
        assert "Flush" == func(cards)

    def test_d(self):
        cards = ['D2', 'D3', 'D4', 'D5', 'D7']
        assert "Flush" == func(cards)

    def test_c(self):
        cards = ['C2', 'C3', 'C4', 'C5', 'C7']
        assert "Flush" == func(cards)

    def test_s(self):
        cards = ['S2', 'S3', 'S4', 'S5', 'S7']
        assert "Flush" == func(cards)

#  A Full Housh
class TestFullHouse:
    def test_1(self):
        cards = ['H2', 'D2', 'C2', 'S5', 'H5']
        assert "A Full House" == func(cards)
    def test_2(self):
        cards = ['H3', 'D3', 'C3', 'S7', 'H7']
        assert "A Full House" == func(cards)
    def test_a(self):
        cards = ['H4', 'D4', 'CA', 'SA', 'HA']
        assert "A Full House" == func(cards)

# Four Of A Kind
class TestFourOfKind:
    def test_1(self):
        cards = ['H2', 'D2', 'C2', 'S2', 'H7']
        assert "Four Of A Kind" == func(cards)
    def test_2(self):
        cards = ['H3', 'D3', 'C3', 'S3', 'H7']
        assert "Four Of A Kind" == func(cards)
    def test_a(self):
        cards = ['H2', 'DA', 'CA', 'SA', 'HA']
        assert "Four Of A Kind" == func(cards)

# Straight Flush
class TestStraightFlush:
    def test_1(self):
        cards = ['H2', 'H3', 'H4', 'H5', 'H6']
        assert "Straight Flush" == func(cards)

    def test_2(self):
        cards = ['D3', 'D4', 'D5', 'D6', 'D7']
        assert "Straight Flush" == func(cards)

    def test_3(self):
        cards = ['C9','C10', 'CJ', 'CQ', 'CK']
        assert "Straight Flush" == func(cards)

# Royal flush
class TestRoyalFlush:
    def test_h(self):
        cards = ['H10', 'HJ', 'HQ', 'HK', 'HA']
        assert "Royal Flush" == func(cards)
    def test_d(self):
        cards = ['D10', 'DJ', 'DQ', 'DK', 'DA']
        assert "Royal Flush" == func(cards)
    def test_c(self):
        cards = ['C10', 'CJ', 'CQ', 'CK', 'CA']
        assert "Royal Flush" == func(cards)
    def test_s(self):
        cards = ['S10', 'SJ', 'SQ', 'SK', 'SA']
        assert "Royal Flush" == func(cards)
