import re
from collections import Counter
from common.common import count_status

def func(cards):

    check_list = count_status(cards)

    if(judge_black_jack(check_list[0])):
        return "Black Jack"

    return "You Lose..."

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
    