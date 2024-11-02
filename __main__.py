#!/usr/bin/env python


import pocer.app as app
import pocer.distribution as distribution


def __init__():
    # sample パッケージを使った処理
    print("あなたの手札は、、、")
    cards = distribution.func()
    print(cards)

    print("")
    print("手札の役は")
    print(app.func(cards))
    print("")


if __name__ == '__main__':
    __init__()
