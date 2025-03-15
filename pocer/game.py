import distribution, app, conversion, judge
import time

def func():
    print("Pocer Quiz!")
    cards = distribution.func()

    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    start = time.time()

    print(cards)
    print("回答を入力せよ")
    print("Royal flush 10")
    print("Straight Flush 9")
    print("Four Of A Kind 8")
    print("A Full House 7")
    print("Flush 6")
    print("Straight 5")
    print("Three Of A Kind 4")
    print("Two Pair 3")
    print("A Pair 2")
    print("High Card 1")
    answer = int(input())
    end = time.time()
    
    result = app.func(cards)
    print("result:" + result)
    print("answer:" + str(conversion.func(answer)))
    answertime = end - start
    scoretime = 10 - answertime
    print("answertime:" + str(answertime))
    print("scoretime:" + str(scoretime))
    if(scoretime < 0):
        print("TimeOut")
        return 0
    # answerを文字に変換
    elif(result == conversion.func(answer)):
        score = judge.func(answer, scoretime)
        print("Score:" + str(score))
        return score
    else:
        print("Miss...")
        return 0
       
if __name__ == '__main__':
    func()
