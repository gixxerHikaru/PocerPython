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

    return (check_number_list[0] * 2 + check_number_list[1] * 3 + check_number_list[2] *
                4 + check_number_list[3] * 5 + check_number_list[4] * 6 + check_number_list[5] * 7 + check_number_list[6] *
                8 + check_number_list[7] * 9 + check_number_list[8] * 10 + check_number_list[9] * 10 + check_number_list[10] *
                10 + check_number_list[11] * 10 + check_number_list[12] * 11)
