from pocer.judge import func

#点数は(役)x(残り時間)
#[Royal flush, Straight Flush, Four Of A Kind, A Full House, Flush, Three Of A Kind, Two Pair, A Pair, High Card] = [10,9,8,7,6,5,4,3,2,1]

# High Card(*1)
class TestHighCard:
    def test_9(self):
        judge = 1
        time = 9.00
        assert 9 == func(judge, time)
    def test_1(self):
        judge = 1
        time = 1.11
        assert 1 == func(judge, time)
    def test_0(self):
        judge = 1
        time = 0.11
        assert 0 == func(judge, time)

# A Pair(*2)
class TestAPair:
    def test_9(self):
        judge = 2
        time = 9.00
        assert 18 == func(judge, time)
    def test_1(self):
        judge = 2
        time = 1.11
        assert 2 == func(judge, time)

# Two Pair(*3)
class TestTwoPair:
    def test_9(self):
        judge = 3
        time = 9.00
        assert 27 == func(judge, time)
    def test_1(self):
        judge = 3
        time = 1.11
        assert 3 == func(judge, time)

# Three Of A Kind(*4)
class TestThreeOfAKind:
    def test_3(self):
        judge = 4
        time = 3.09
        assert 12 == func(judge, time)
    def test_1(self):
        judge = 4
        time = 1.11
        assert 4 == func(judge, time)

# Straight(*5)
class TestStraight:
    def test_4(self):
        judge = 5
        time = 4.44
        assert 20 == func(judge, time)
    def test_2(self):
        judge = 5
        time = 2.22
        assert 10 == func(judge, time)
    def test_0(self):
        judge = 5
        time = 0.21
        assert 0 == func(judge, time)
        
# Flush(*6)
class TestFlush:
    def test_5(self):
        judge = 6
        time = 5.44
        assert 30 == func(judge, time)
    def test_3(self):
        judge = 6
        time = 3.94
        assert 18 == func(judge, time)
    def test_1(self):
        judge = 6
        time = 1.88
        assert 6 == func(judge, time)
    def test_0(self):
        judge = 6
        time = 0.99
        assert 0 == func(judge, time)

# A Full House(*7)
class TestAFullHouse:
    def test_6(self):
        judge = 7
        time = 6.66
        assert 42 == func(judge, time)
    def test_4(self):
        judge = 7
        time = 4.84
        assert 28 == func(judge, time)
    def test_2(self):
        judge = 7
        time = 2.89
        assert 14 == func(judge, time)
    def test_0(self):
        judge = 7
        time = 0.99
        assert 0 == func(judge, time)

# Four Of A Kind(*8)
class TestFourOfAKind:
    def test_7(self):
        judge = 8
        time = 7.77
        assert 56 == func(judge, time)
    def test_5(self):
        judge = 8
        time = 5.05
        assert 40 == func(judge, time)
    def test_3(self):
        judge = 8
        time = 3.60
        assert 24 == func(judge, time)
    def test_1(self):
        judge = 8
        time = 1.11
        assert 8 == func(judge, time)

# Straight Flush(*9)
class TestStraightFlush:
    def test_8(self):
        judge = 9
        time = 8.99
        assert 72 == func(judge, time)
    def test_6(self):
        judge = 9
        time = 6.02
        assert 54 == func(judge, time)
    def test_4(self):
        judge = 9
        time = 4.70
        assert 36 == func(judge, time)
    def test_2(self):
        judge = 9
        time = 2.88
        assert 18 == func(judge, time)

# Royal flush(*10)
class TestRoyalFlush:
    def test_9(self):
        judge = 10
        time = 9.00
        assert 90 == func(judge, time)
    def test_7(self):
        judge = 10
        time = 7.01
        assert 70 == func(judge, time)
    def test_5(self):
        judge = 10
        time = 5.50
        assert 50 == func(judge, time)
    def test_3(self):
        judge = 10
        time = 3.33
        assert 30 == func(judge, time)
        