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

# Straight
def test_straight1():
    cards = ['H2', 'D3', 'C4', 'S5', 'H6']
    assert "Straight" == func(cards)

def test_straight2():
    cards = ['H3', 'D4', 'C5', 'S6', 'H7']
    assert "Straight" == func(cards)

def test_straightA():
    cards = ['H10', 'DJ', 'CQ', 'SK', 'HA']
    assert "Straight" == func(cards)

# flush
def test_flush_h():
    cards = ['H2', 'H3', 'H4', 'H5', 'H7']
    assert "Flush" == func(cards)

def test_flush_d():
    cards = ['D2', 'D3', 'D4', 'D5', 'D7']
    assert "Flush" == func(cards)

def test_flush_c():
    cards = ['C2', 'C3', 'C4', 'C5', 'C7']
    assert "Flush" == func(cards)

def test_flus_s():
    cards = ['S2', 'S3', 'S4', 'S5', 'S7']
    assert "Flush" == func(cards)

#  A Full Housh
def test_full_housh1():
    cards = ['H2', 'D2', 'C2', 'S5', 'H5']
    assert "A Full House" == func(cards)
def test_full_housh2():
    cards = ['H3', 'D3', 'C3', 'S7', 'H7']
    assert "A Full House" == func(cards)
def test_full_houshA():
    cards = ['H4', 'D4', 'CA', 'SA', 'HA']
    assert "A Full House" == func(cards)

# Four Of A Kind
def test_four_of_a_kind1():
    cards = ['H2', 'D2', 'C2', 'S2', 'H7']
    assert "Four Of A Kind" == func(cards)
def test_four_of_a_kind2():
    cards = ['H3', 'D3', 'C3', 'S3', 'H7']
    assert "Four Of A Kind" == func(cards)
def test_four_of_a_kindA():
    cards = ['H2', 'DA', 'CA', 'SA', 'HA']
    assert "Four Of A Kind" == func(cards)

# Straight Flush
def test_straight_flush1():
    cards = ['H2', 'H3', 'H4', 'H5', 'H6']
    assert "Straight Flush" == func(cards)

def test_straight_flush2():
    cards = ['D3', 'D4', 'D5', 'D6', 'D7']
    assert "Straight Flush" == func(cards)

def test_straight_flush3():
    cards = ['C9','C10', 'CJ', 'CQ', 'CK']
    assert "Straight Flush" == func(cards)

# Royal flush
def test_royal_flush_h():
    cards = ['H10', 'HJ', 'HQ', 'HK', 'HA']
    assert "Royal Flush" == func(cards)
def test_royal_flush_d():
    cards = ['D10', 'DJ', 'DQ', 'DK', 'DA']
    assert "Royal Flush" == func(cards)
def test_royal_flush_c():
    cards = ['C10', 'CJ', 'CQ', 'CK', 'CA']
    assert "Royal Flush" == func(cards)
def test_royal_flush_s():
    cards = ['S10', 'SJ', 'SQ', 'SK', 'SA']
    assert "Royal Flush" == func(cards)
