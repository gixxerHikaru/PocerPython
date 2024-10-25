import re
from collections import Counter

def func(cards):

    check_number_list = count_number_status(cards)
    check_suit_list = count_suit_status(cards)

    check_flush = judge_flush(check_suit_list)

    if(check_flush):
        for i in range(len(check_number_list) - 4):
            if all(check_number_list[i + j] == 1 for j in range(5)):
                if(i == 8):
                    return "Royal Flush"
                else:
                    return "Straight Flush"
        return "Flush"

    for i in range(len(check_number_list) - 4):
        if all(check_number_list[i + j] == 1 for j in range(5)):
            return "Straight" 
        
    four_of_count = 0
    for x in check_number_list:
        if(x == 4):
            four_of_count += 1
    if(four_of_count):
        return "Four Of A Kind"

    three_of_count = 0
    for x in check_number_list:
        if(x == 3):
            three_of_count += 1

    
    pair_count = 0
    for x in check_number_list:
        if(x == 2):
            pair_count += 1
    if(three_of_count and pair_count):
        return "A Full House"
    if(three_of_count):
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

    for x in cards:
        if(re.search('2', x)):
            count_2 += 1
        elif(re.search('3', x)):
            count_3 += 1
        elif(re.search('4', x)):
            count_4 += 1
        elif(re.search('5', x)):
            count_5 += 1            
        elif(re.search('6', x)):
            count_6 += 1
        elif(re.search('7', x)):
            count_7 += 1
        elif(re.search('8', x)):
            count_8 += 1
        elif(re.search('9', x)):
            count_9 += 1
        elif(re.search('10', x)):
            count_10 += 1
        elif(re.search('J', x)):
            count_j += 1
        elif(re.search('Q', x)):
            count_q += 1
        elif(re.search('K', x)):
            count_k += 1
        elif(re.search('A', x)):
            count_a += 1
    return [count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10, count_j, count_q, count_k, count_a]

def count_suit_status(cards):
    count_h = 0
    count_c = 0
    count_d = 0
    count_s = 0

    for x in cards:
        if(re.search('H', x)):
            count_h += 1
        elif(re.search('C', x)):
            count_c += 1
        elif(re.search('D', x)):
            count_d += 1
        elif(re.search('S', x)):
            count_s += 1

    return [count_h, count_c, count_d, count_s]

def judge_flush(check_suit_list):
    for x in check_suit_list:
        if(x == 5):
            return True
        