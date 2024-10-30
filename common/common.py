import re


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
