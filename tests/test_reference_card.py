import re

from pocer.reference_card import func

class TestSuitCheck:
    def test_club_one(self):
        card = "CA"
        pattern = "/Users/sakuraiyuuki/Documents/GitHub/PocerPython/pocer/image/cards/CA.png"
        assert re.match(pattern, func(card))
    def test_club_second(self):
        card = "C2"
        pattern = "/Users/sakuraiyuuki/Documents/GitHub/PocerPython/pocer/image/cards/C2.png"
        assert re.match(pattern, func(card))        
        