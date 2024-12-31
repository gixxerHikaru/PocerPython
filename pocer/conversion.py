def func(answer):
    if(answer == 10):
        return "Royal Flush"
    elif(answer == 9):
        return "Straight Flush"
    elif(answer == 8):
        return "Four Of A Kind"
    elif(answer == 7):
        return "A Full House"
    elif(answer == 6):
        return "Flush"
    elif(answer == 5):
        return "Straight"
    elif(answer == 4):
        return "Three Of A Kind"
    elif(answer == 3):
        return "Two Pair"
    elif(answer == 2):
        return "A Pair"
    elif(answer == 1):
        return "High Card"
    else:
        return None
    