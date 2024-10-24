from app import func

def test_highcard():
    cards = ['H2', 'D3', 'C3', 'S4', 'H6']
    assert "High Card" == func(cards)
