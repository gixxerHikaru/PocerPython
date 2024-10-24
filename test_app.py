from app import func

def test_highcard():
    cards = ['H2', 'D3', 'C4', 'S5', 'H7']
    assert "High Card" == func(cards)
