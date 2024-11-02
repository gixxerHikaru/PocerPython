#!/usr/bin/env python


import pocer.app as app
import pocer.distribution as distribution


def __init__():
    print("メニューを選択してください。１：ポーカー　２：ブラックジャック(整備中)")
    menu_select = input('>> ')

    print("選択メニュー： " + menu_select)

    # メニュー[1] ポーカー選択時
    if(menu_select == '1'):
        print("ポーカーモード")
        print("")
        # sample パッケージを使った処理
        print("あなたの手札は、、、")
        cards = distribution.func()
        print(cards)

        print("")
        print("手札の役は")
        print(app.func(cards))
        print("")

    # メニュー[2] ブラックジャック選択時
    elif(menu_select == '2'):
        print("ブラックジャックモード")
        print("")
        print("現在整備中です。お楽しみに")

    else:
        print("そのメニューは存在しません。")

    print("")
    print("終了します。")

if __name__ == '__main__':
    __init__()
