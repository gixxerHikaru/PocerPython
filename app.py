import re
from collections import Counter

def func(cards):

    check_list = count_status(cards)

    check_flush = judge_flush(check_list[1])
    check_straight = judge_straight(check_list[0])
    if(check_flush):
        if(check_straight == 2):
            return "Royal Flush"
        elif(check_straight == 1):
            return "Straight Flush"
        return "Flush"
    if(check_straight):
        return "Straight"

    check_four_of_kind = judge_four_of_kind(check_list[0])
    if(check_four_of_kind):
        return "Four Of A Kind"

    check_three_of_count = judge_three_of_count(check_list[0])
    pair_count = count_pair(check_list[0])
    if(check_three_of_count and pair_count):
        return "A Full House"
    if(check_three_of_count):
        return "Three Of A Kind"
    if(pair_count == 2):
        return "Two Pair"
    if(pair_count == 1):
        return "A Pair"

    return "High Card"

def count_status(cards):

    # 2~10,J,Q,K,Aの順でカードの枚数を確保するリスト
    count_number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # H,C,D,Sの順でカードの枚数を確保するリスト
    count_suit_list = [0, 0, 0, 0]
    suit_list = ['H', 'C', 'D', 'S']

    # cardsのnumberとsuitを数える
    for x in cards:
        # cardのnumberを数える
        search_card(x, number_list, count_number_list)
        # cardのsuitを数える
        search_card(x, suit_list, count_suit_list)

    return [count_number_list , count_suit_list]

def search_card(card, list, count_list):
    for i in range(len(list)):
        if(re.search(list[i], card)):
            count_list[i] += 1

def judge_flush(check_suit_list):
    for x in check_suit_list:
        if(x == 5):
            return True

def judge_straight(check_number_list):
    for i in range(len(check_number_list) - 4):
        if all(check_number_list[i + j] == 1 for j in range(5)):
            if(i == 8):
                return 2
            else:
                return 1

def judge_four_of_kind(check_number_list):
    four_of_count = 0
    for x in check_number_list:
        if(x == 4):
            four_of_count += 1
    if(four_of_count):
        return True    

def judge_three_of_count(check_number_list):
    for x in check_number_list:
        if(x == 3):
            return True

def count_pair(check_number_list):
    pair_count = 0
    for x in check_number_list:
            if(x == 2):
                pair_count += 1
    return pair_count
