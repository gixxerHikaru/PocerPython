import sys, random
import pygame
import distribution, reference_card
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font(None, 55)   
card_font = pygame.font.Font(None, 25)   
title = font.render("Pocer Quiz", True, white)
SIMPLE_IMAGE_PATH = "/Users/sakuraiyuuki/Documents/GitHub/PocerPython/pocer/image/cards/card_back.png"
card_back = pygame.image.load(SIMPLE_IMAGE_PATH)
card_back = pygame.transform.scale(card_back, (68.25,100))
button = pygame.Rect(265, 260, 80, 40)
button_font = pygame.font.Font(None, 30)
start_button = button_font.render("Start!!", True, white)
# 繰り返し画面を描画 --- (*2)
running = True
start_screen = True
next_screen = False
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
         pygame.draw.rect(screen, (0,125,125), pygame.Rect(100, 50, 400, 300))

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
         answer_y = 160
         answer_positions = [(answer_x, answer_y), (answer_x + 200, answer_y),
                             (answer_x, answer_y + 40), (answer_x + 200, answer_y + 40),
                             (answer_x, answer_y + 80), (answer_x + 200, answer_y + 80),
                             (answer_x, answer_y + 120), (answer_x + 200, answer_y + 120),
                             (answer_x, answer_y + 160), (answer_x + 200, answer_y + 160),]
        
         # カードの表示
         for i in range(5):
             screen.blit(cards[i], card_positions[i])

         pygame.display.update()
         pygame.time.wait(5000)
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
                    
