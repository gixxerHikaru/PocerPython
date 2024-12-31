
def func(judge, time):
    if(judge == "Royal Flush"):
        return 10 * int(time)
    elif(judge == "Straight Flush"):
        return 9 * int(time)
    elif(judge == "Four Of A Kind"):
        return 8 * int(time)
    elif(judge == "A Full House"):
        return 7 * int(time)
    elif(judge == "Flush"):
        return 6 * int(time)
    elif(judge == "Straight"):
        return 5 * int(time)
    elif(judge == "Three Of A Kind"):
        return 4 * int(time)
    elif(judge == "Two Pair"):
        return 3 * int(time)
    elif(judge == "A Pair"):
        return 2 * int(time)
    elif(judge == "High Card"):
        return 1 * int(time)
    return 0
