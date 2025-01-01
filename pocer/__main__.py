#!/usr/bin/env python


import game
import time

def __init__():
    # ポーカー・ジャッジゲーム
    score = []
    for i in range(5):
        if(i != 0):
            print("NextGame")
        time.sleep(1)
        score.append(game.func())
    
    print("Total Score:" + str(score) + " = " + str(sum(score)))

if __name__ == '__main__':
    __init__()
