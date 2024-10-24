from app import func

def test_high_card():
    cards = ['H2', 'D3', 'C4', 'S5', 'H7']
    assert "High Card" == func(cards)

def test_a_pair1():
    cards = ['H2', 'D2', 'C4', 'S5', 'H7']
    assert "A Pair" == func(cards)

def test_a_pair2():
    cards = ['H3', 'D3', 'C4', 'S5', 'H7']
    assert "A Pair" == func(cards)

def test_a_pairA():
    cards = ['H2', 'D3', 'C4', 'SA', 'HA']
    assert "A Pair" == func(cards)
