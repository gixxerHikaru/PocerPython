from pocer.distribution import func
# テスト使い方
# 全通し pytest test_distribution.py
# クラス実行 pytest test_distribution.py::TestDistribution


# Distribution
class TestDistribution:
    def test_distribution_one(self):
        
        assert 'H2' == func()[0]

    def test_distribution_second(self):
    
        assert 'D3' == func()[1]

    def test_distribution_third(self):
        
        assert 'C4' == func()[2]

    def test_distribution_fourth(self):
        
        assert 'S5' == func()[3]

    def test_distribution_fifth(self):
        
        assert 'H7' == func()[4]                    
