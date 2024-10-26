import re
from collections import Counter

def func(cards):

    check_number_list = count_number_status(cards)
    check_suit_list = count_suit_status(cards)

    check_flush = judge_flush(check_suit_list)
    check_straight = judge_straight(check_number_list)
    if(check_flush):
        if(check_straight == 2):
            return "Royal Flush"
        elif(check_straight == 1):
            return "Straight Flush"
        return "Flush"
    if(check_straight):
        return "Straight"

    check_four_of_kind = judge_four_of_kind(check_number_list)
    if(check_four_of_kind):
        return "Four Of A Kind"

    check_three_of_count = judge_three_of_count(check_number_list)
    pair_count = count_pair(check_number_list)
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

    for x in cards:
        if(re.search('2', x)):
            count_list[0] += 1
        elif(re.search('3', x)):
            count_list[1] += 1
        elif(re.search('4', x)):
            count_list[2] += 1
        elif(re.search('5', x)):
            count_list[3] += 1            
        elif(re.search('6', x)):
            count_list[4] += 1
        elif(re.search('7', x)):
            count_list[5] += 1
        elif(re.search('8', x)):
            count_list[6] += 1
        elif(re.search('9', x)):
            count_list[7] += 1
        elif(re.search('10', x)):
            count_list[8] += 1
        elif(re.search('J', x)):
            count_list[9] += 1
        elif(re.search('Q', x)):
            count_list[10] += 1
        elif(re.search('K', x)):
            count_list[11] += 1
        elif(re.search('A', x)):
            count_list[12] += 1

    return count_list

def count_suit_status(cards):
    count_h = 0
    count_c = 0
    count_d = 0
    count_s = 0

    count_list = [count_h, count_c, count_d, count_s]

    for x in cards:
        if(re.search('H', x)):
            count_list[0] += 1
        elif(re.search('C', x)):
            count_list[1] += 1
        elif(re.search('D', x)):
            count_list[2] += 1
        elif(re.search('S', x)):
            count_list[3] += 1

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
