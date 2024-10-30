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

# Not Include A
class TestNotIncludeA():
    def test_4(self):
        cards = ['H2', 'C2']
        assert "4" == func(cards)

    def test_5(self):
        cards = ['C2', 'C3']
        assert "5" == func(cards)

    def test_6(self):
        cards = ['H3', 'C3']
        assert "6" == func(cards)

    def test_7(self):
        cards = ['D3', 'S4']
        assert "7" == func(cards)

    def test_8(self):
        cards = ['H4', 'C4']
        assert "8" == func(cards)

    def test_9(self):
        cards = ['C2', 'C7']
        assert "9" == func(cards)

    def test_10(self):
        cards = ['H5', 'C5']
        assert "10" == func(cards)

    def test_11(self):
        cards = ['D5', 'S6']
        assert "11" == func(cards)

    def test_12(self):
        cards = ['H6', 'C6']
        assert "12" == func(cards)

    def test_13(self):
        cards = ['C6', 'C7']
        assert "13" == func(cards)

    def test_14(self):
        cards = ['H7', 'C7']
        assert "14" == func(cards)

    def test_15(self):
        cards = ['D7', 'S8']
        assert "15" == func(cards)

    def test_16(self):
        cards = ['H8', 'C8']
        assert "16" == func(cards)

    def test_17(self):
        cards = ['C8', 'C9']
        assert "17" == func(cards)

    def test_18(self):
        cards = ['H9', 'C9']
        assert "18" == func(cards)

    def test_19(self):
        cards = ['D9', 'SJ']
        assert "19" == func(cards)

    def test_20(self):
        cards = ['DJ', 'SJ']
        assert "20" == func(cards)

# Include A
class TestIncludeA():
    class TestOverA():
        class TestMultipleA():
            def test_double(self):
                cards = ['HA', 'CA']
                assert "12" == func(cards)
            
            def test_triple(self):
                cards = ['HA', 'CA', 'DA']
                assert "13" == func(cards)
            
            def test_all(self):
                cards = ['HA', 'CA', 'DA', 'SA']
                assert "14" == func(cards)            
            
        def test_13(self):
            cards = ['H10', 'C2', 'HA']
            assert "13" == func(cards)
        
        def test_14(self):
            cards = ['H9', 'C4', 'DA']
            assert "14" == func(cards)

        def test_15(self):
            cards = ['D8', 'S6', 'CA']
            assert "15" == func(cards)

        def test_16(self):
            cards = ['H8', 'C7', 'SA']
            assert "16" == func(cards)

        def test_17(self):
            cards = ['C8', 'C8', 'CA']
            assert "17" == func(cards)

        def test_18(self):
            cards = ['H7', 'C7', 'D3', 'SA']
            assert "18" == func(cards)

        def test_19(self):
            cards = ['D2', 'S2', 'C2', 'H2', 'D3', 'S3', 'C4', 'SA']
            assert "19" == func(cards)

        def test_20(self):
            cards = ['D2', 'S2', 'C2', 'H2', 'D3', 'S4', 'C4', 'SA']
            assert "20" == func(cards)

        def test_21(self):
            cards = ['D2', 'S2', 'C2', 'H2', 'D3', 'S3', 'C3', 'H3' ,'SA']
            assert "21" == func(cards)


    def test_13(self):
        cards = ['CA', 'C2']
        assert "13" == func(cards)

    def test_14(self):
        cards = ['HA', 'C3']
        assert "14" == func(cards)

    def test_15(self):
        cards = ['DA', 'S4']
        assert "15" == func(cards)

    def test_16(self):
        cards = ['HA', 'C5']
        assert "16" == func(cards)

    def test_17(self):
        cards = ['CA', 'C6']
        assert "17" == func(cards)

    def test_18(self):
        cards = ['HA', 'C7']
        assert "18" == func(cards)

    def test_19(self):
        cards = ['DA', 'S8']
        assert "19" == func(cards)

    def test_20(self):
        cards = ['DA', 'S9']
        assert "20" == func(cards)

# Lose
class TestLose:
    def test_22(self):
        cards = ['HK', 'H10', 'H2']
        assert "You Lose..." == func(cards)

    def test_23(self):
        cards = ['CQ', 'C9', 'C4']
        assert "You Lose..." == func(cards)

    def test_24(self):
        cards = ['HJ', 'C8', 'D6']
        assert "You Lose..." == func(cards)

    def test_25(self):
        cards = ['D4', 'S5', 'C6', 'HK']        assert "You Lose..." == func(cards) 