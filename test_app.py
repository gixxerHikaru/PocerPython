from app import func

# High Card
def test_high_card():
    cards = ['H2', 'D3', 'C4', 'S5', 'H7']
    assert "High Card" == func(cards)

# A Pair
def test_a_pair1():
    cards = ['H2', 'D2', 'C4', 'S5', 'H7']
    assert "A Pair" == func(cards)

def test_a_pair2():
    cards = ['H3', 'D3', 'C4', 'S5', 'H7']
    assert "A Pair" == func(cards)

def test_a_pairA():
    cards = ['H2', 'D3', 'C4', 'SA', 'HA']
    assert "A Pair" == func(cards)

# Two Pair
def test_two_pair1():
    cards = ['H2', 'D2', 'C4', 'S4', 'H7']
    assert "Two Pair" == func(cards)

def test_two_pair2():
    cards = ['H3', 'D3', 'C5', 'S5', 'H7']
    assert "Two Pair" == func(cards)

def test_two_pairA():
    cards = ['H2', 'D4', 'C4', 'SA', 'HA']
    assert "Two Pair" == func(cards)

# Three Of A Kind
def test_three_of_a_kind1():
    cards = ['H2', 'D2', 'C2', 'S5', 'H7']
    assert "Three Of A Kind" == func(cards)
def test_three_of_a_kind2():
    cards = ['H3', 'D3', 'C3', 'S5', 'H7']
    assert "Three Of A Kind" == func(cards)
def test_three_of_a_kindA():
    cards = ['H2', 'D4', 'CA', 'SA', 'HA']
    assert "Three Of A Kind" == func(cards)
