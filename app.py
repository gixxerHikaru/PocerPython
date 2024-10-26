import re
from collections import Counter

def func(cards):

    check_list = [count_number_status(cards), count_suit_status(cards)]

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

def count_number_status(cards):
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_j = 0
    count_q = 0
    count_k = 0
    count_a = 0

    count_list = [count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,
                   count_10, count_j, count_q, count_k, count_a]
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # cardsのnumberを数える
    for x in cards:
        for y in range(len(number_list)):
            if(re.search(number_list[y], x)):
                count_list[y] += 1

    return count_list

def count_suit_status(cards):
    count_h = 0
    count_c = 0
    count_d = 0
    count_s = 0

    count_list = [count_h, count_c, count_d, count_s]
    suit_list = ['H', 'C', 'D', 'S']

    # cardsのsuitを数える
    for x in cards:
        for y in range(len(suit_list)):
            if(re.search(suit_list[y], x)):
                count_list[y] += 1

    return count_list

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
