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

    if(count_2 == 2 or count_3 == 2 or count_4 == 2 or count_5 == 2 or count_6 == 2 or count_7 == 2 or count_8 == 2 or count_9 == 2 or count_10 == 2 or count_J == 2 or count_Q == 2 or count_K == 2 or count_A == 2):
        return "A Pair"

    return "High Card"
