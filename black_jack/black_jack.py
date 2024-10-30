import re
from collections import Counter
from common.common import count_status

def func(cards):

    check_list = count_status(cards)

    if(judge_black_jack(check_list[0])):
        return "Black Jack"

    score = count_score(check_list[0])

    if(score > 21):
        return "You Lose..."
    else:
        return str(score)

def judge_black_jack(check_number_list):
    count = 0
    for x in check_number_list:
        if(count == 8 or count == 12):
            continue
        elif(x > 0):
            return False
        count += 1

    if(check_number_list[8] == 1 and check_number_list[12] == 1):
        return True
    
def count_score(check_number_list):
    
    ace_score = 0    
    if(check_number_list[12] == 0):
        ace_score = 0
    elif(check_number_list[12] == 1):
        ace_score = 11
    elif(check_number_list[12] == 2):
        ace_score = 12
    elif(check_number_list[12] == 3):
        ace_score = 13
    elif(check_number_list[12] == 4):
        ace_score = 14
    
    score = (check_number_list[0] * 2 + check_number_list[1] * 3 + check_number_list[2] *
                4 + check_number_list[3] * 5 + check_number_list[4] * 6 + check_number_list[5] * 7 + check_number_list[6] *
                8 + check_number_list[7] * 9 + check_number_list[8] * 10 + check_number_list[9] * 10 + check_number_list[10] *
                10 + check_number_list[11] * 10 + ace_score)

    if(score <= 21):
        return score
    else:
        return (check_number_list[0] * 2 + check_number_list[1] * 3 + check_number_list[2] *
                4 + check_number_list[3] * 5 + check_number_list[4] * 6 + check_number_list[5] * 7 + check_number_list[6] *
                8 + check_number_list[7] * 9 + check_number_list[8] * 10 + check_number_list[9] * 10 + check_number_list[10] *
                10 + check_number_list[11] * 10 + check_number_list[12] * 1)
