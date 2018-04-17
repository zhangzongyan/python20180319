'''
作者: zhangzongyan
时间: 18-4-17
'''
import pygame
from pygame.locals import *
#模块中包含游戏中的常量,比如按键值
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("检测按键时间")

# background
bg = pygame.image.load("../images/bg.png")
nl_img = pygame.image.load("../images/niulang.png")
nl_rect = nl_img.get_rect()
print(nl_rect.width, nl_rect.height)

# clock控制速度
clock = pygame.time.Clock()

step = 5
move = {K_UP:0, K_DOWN:0, K_LEFT:0, K_RIGHT:0}
x, y = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
        elif event.type == KEYDOWN:
            # 按键了---->哪个键
            if event.key in move:
                move[event.key] = step
        elif event.type == KEYUP:
            if event.key in move:
                move[event.key] = 0
    x += move[K_RIGHT]
    x -= move[K_LEFT]
    y -= move[K_UP]
    y += move[K_DOWN]
    # 将背景填充白色
    screen.fill((255,255,255))
    screen.blit(bg, (0, 0))
    # 画牛郎
    screen.blit(nl_img, (x, y))

    pygame.display.update()
    clock.tick(60)

