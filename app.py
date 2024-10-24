import re
from collections import Counter

def func(cards):

    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_J = 0
    count_Q = 0
    count_K = 0
    count_A = 0

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
            count_J += 1
        elif(re.search('Q', x)):
            count_Q += 1
        elif(re.search('K', x)):
            count_K += 1
        elif(re.search('A', x)):
            count_A += 1                        

    check_list = [count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10, count_J, count_Q, count_K, count_A]

    count_h = 0
    count_d = 0
    count_c = 0
    count_s = 0

    for x in cards:
        if(re.search('H', x)):
            count_h += 1
        elif(re.search('D', x)):
            count_d += 1
        elif(re.search('C', x)):
            count_c += 1
        elif(re.search('S', x)):
            count_s += 1  

    if(count_h == 5 or count_d == 5 or count_c == 5 or count_s == 5):
        for i in range(len(check_list) - 4):
            if all(check_list[i + j] == 1 for j in range(5)):
                return "Straight Flush"

    if(count_h == 5 or count_d == 5 or count_c == 5 or count_s == 5):
        return "Flush"

    for i in range(len(check_list) - 4):
        if all(check_list[i + j] == 1 for j in range(5)):
            return "Straight" 
        
    four_of_count = 0
    for x in check_list:
        if(x == 4):
            four_of_count += 1
    if(four_of_count):
        return "Four Of A Kind"

    three_of_count = 0
    for x in check_list:
        if(x == 3):
            three_of_count += 1

    
    pair_count = 0
    for x in check_list:
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
