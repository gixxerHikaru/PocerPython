import sys
import pygame
import distribution, reference_card, app, conversion
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font(None, 55)
font30 = pygame.font.Font(None, 30)   
card_font = pygame.font.Font(None, 25)   
title = font.render("Pocer Quiz", True, white)
SIMPLE_IMAGE_PATH = "pocer/image/cards/card_back.png"
card_back = pygame.image.load(SIMPLE_IMAGE_PATH)
card_back = pygame.transform.scale(card_back, (68.25,100))
button = pygame.Rect(265, 260, 80, 40)
button_font = pygame.font.Font(None, 30)
start_button = button_font.render("Start!!", True, white)
answer_display = pygame.Rect(150, 80, 300, 250)
round_display = pygame.Rect(150, 80, 300, 100)
# 繰り返し画面を描画 --- (*2)
running = True
start_screen = True
next_screen = False

def quiz():
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.circle(screen, (0,125,125), (300,200), 150) # 円を描画
        screen.blit(font.render("3", True, white), [300, 200])
        pygame.display.update()
        pygame.time.wait(1000)
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.circle(screen, (0,125,125), (300,200), 150) # 円を描画
        screen.blit(font.render("2", True, white), [300, 200])
        pygame.display.update()
        pygame.time.wait(1000)
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.circle(screen, (0,125,125), (300,200), 150) # 円を描画
        screen.blit(font.render("1", True, white), [300, 200])
        pygame.display.update()
        pygame.time.wait(1000)
        # 手札表示
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.rect(screen, (0,125,125), pygame.Rect(100, 50, 400, 320))

        card = distribution.func()

        cards = []
        for i in range(5):
            card_path = reference_card.func(card[i])
            card_image = pygame.image.load(card_path)
            card_image = pygame.transform.scale(card_image, (68.25, 100))
            cards.append(card_image)
        card_height = 60
        card_positions = [(120, card_height), (190, card_height), (260, card_height),
                        (330, card_height), (400, card_height)]
        
        answer_x = 130
        answer_y = 180
        answer_positions = [(answer_x, answer_y), (answer_x + 200, answer_y),
                            (answer_x, answer_y + 40), (answer_x + 200, answer_y + 40),
                            (answer_x, answer_y + 80), (answer_x + 200, answer_y + 80),
                            (answer_x, answer_y + 120), (answer_x + 200, answer_y + 120),
                            (answer_x, answer_y + 160), (answer_x + 200, answer_y + 160),]
        answer_button_font = pygame.font.Font(None, 25)
        answer_texts = ["High Card", "A Pair", "Two Pair", "Three Of A Kind", "Straight",
            "Flush", "A Full House", "Four Of A Kind", "Straight Flush", "Royal Flush"]
        answer_buttons = []  # ボタンオブジェクトを格納するリスト

        for i in range(10):
            answer_button = pygame.Rect(answer_positions[i][0], answer_positions[i][1], 120, 20)
            pygame.draw.rect(screen, (100, 0, 250), answer_button)
            answer_buttons.append(answer_button)  # ボタンオブジェクトをリストに追加

            answer_text = answer_button_font.render(answer_texts[i], True, white)
            screen.blit(answer_text, answer_positions[i])
        
        # カードの表示
        for i in range(5):
            screen.blit(cards[i], card_positions[i])
        answer_number = 0
        pygame.display.update()

        your_answer_text = None
        wait_time = 5000
        wait_start_time = pygame.time.get_ticks()
        wait_active = True
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, answer_button in enumerate(answer_buttons):  # 各ボタンについて判定
                        if answer_button.collidepoint(event.pos):
                            wait_finish_time = pygame.time.get_ticks()
                            print(f"{i+1} button was pressed")
                            answer_number = i + 1
                            your_answer_text = answer_texts[i]
                            wait_active = False
            if wait_active:
                # 待機時間が経過していない場合
                elapsed_time = pygame.time.get_ticks() - wait_start_time
                remaining_time = wait_time - elapsed_time
                if remaining_time <= 0:
                    # 待機時間終了
                    wait_active = False
                    screen.fill(black) # 背景を黒で塗りつぶす
                    pygame.draw.rect(screen, (100, 0, 250), round_display)
                    screen.blit(button_font.render("Time Over...", True, white), [150, 100])
                    pygame.display.update()
                    pygame.time.wait(1000)
                    print("待機時間終了")
                    remaining_time = 0
            pygame.display.update()
            if wait_active:
                # 待機中は短い遅延を入れる
                pygame.time.delay(10)
            else:
                # 待機が終了したら、次の処理へ
                print("待機ループ終了。次の処理を実行")
                break  # while ループを抜ける               

        # ここに time.wait() 後の処理を記述
        print("time.wait() 後の処理")
        # 回答表示
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.rect(screen, (0,125,125), pygame.Rect(100, 50, 400, 320))
        screen.blit(button_font.render("Your Answer is ", True, white), [150, 100])
        screen.blit(font.render(conversion.func(answer_number), True, white), [170, 150])
        pygame.display.update()
        pygame.time.wait(2000)
        screen.blit(button_font.render("Answer is ", True, white), [150, 200])
        screen.blit(font.render(app.func(card), True, white), [170, 250])
        pygame.display.update()
        pygame.time.wait(2000)
        # 回答確認
        card_answer_text = app.func(card)
        pygame.draw.rect(screen, (100, 0, 250), answer_display)
        if your_answer_text == card_answer_text:
            screen.blit(font.render("Right!!!", True, black), [200, 100])
        else:
            screen.blit(font.render("False...", True, black), [200, 100])
            answer_number = 0
        pygame.display.update()
        pygame.time.wait(1000)
        screen.blit(font30.render("Pocer Role Score is", True, black), [150, 150])
        fibonacci = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        score = fibonacci[answer_number]
        screen.blit(font.render(str(score), True, black), [350, 140])
        screen.blit(font.render("x", True, black), [350, 170])
        screen.blit(font30.render("Remaining Time is", True, black), [150, 210])
        if remaining_time <= 0:
            answer_time = 0
        else:
            answer_time = (wait_time - (wait_finish_time - wait_start_time))*0.001
        screen.blit(font.render(str(format(answer_time, '.3f')), True, black), [350, 200])
        pygame.display.update()
        pygame.time.wait(1000)
        screen.blit(font30.render("Your Score is", True, black), [150, 250])
        score = score * answer_time
        screen.blit(font.render(str(format(score, '.3f')), True, black), [350, 240])
        pygame.display.update()
        pygame.time.wait(3000)           
        return score

while running:
    if start_screen:
        # 背景と円を描画 --- (*3)
        screen.fill(black) # 背景を黒で塗りつぶす
        pygame.draw.circle(screen, (0,125,125), (300,200), 150) # 円を描画
        screen.blit(title, [200, 100])
        screen.blit(card_back, [200, 150])
        screen.blit(card_back, [270, 150])
        screen.blit(card_back, [340, 150])
        pygame.draw.rect(screen, (100, 0, 250), button)
        screen.blit(start_button, [270, 270])
        # 画面を更新 --- (*4)
    if next_screen:
        sentence = ["Round1", "Round2", "Round3"]
        scores = []
        for i in sentence:
            screen.fill(black) # 背景を黒で塗りつぶす
            pygame.draw.rect(screen, (100, 0, 250), round_display)
            screen.blit(font.render(i, True, white), [200, 100])
            pygame.display.update()
            pygame.time.wait(1000)
            scores.append(quiz())
        # 得点表示
        screen.fill(black)
        pygame.draw.rect(screen, (100, 0, 250), answer_display)
        screen.blit(font.render("Total Score is...", True, white), [150, 100])
        screen.blit(font.render("Round1: " + str(format(scores[0], '.3f')), True, white), [150, 130])
        screen.blit(font.render("Round2: " + str(format(scores[1], '.3f')), True, white), [150, 160])
        screen.blit(font.render("Round3: " + str(format(scores[2], '.3f')), True, white), [150, 190])
        pygame.display.update()
        pygame.time.wait(1000)
        screen.blit(font.render("Total:" + str(format(scores[0]+scores[1]+scores[2], '.3f')), True, white), [150, 250])
        pygame.display.update()
        pygame.time.wait(2000)

        start_screen = True
        next_screen = False

    pygame.display.update()
    # 終了イベントを確認 --- (*5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    print("start button was pressed")
                    start_screen = False
                    next_screen = True
                    