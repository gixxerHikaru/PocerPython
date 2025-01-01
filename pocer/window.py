import sys, random
import pygame
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font(None, 55)   
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
         screen.fill(black) # 背景を黒で塗りつぶす
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
                    
