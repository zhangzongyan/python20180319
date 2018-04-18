'''
作者: zhangzongyan
时间: 18-4-18
'''
import pygame
from pygame.locals import  *
import plane

def main():
    # 初始化游戏
    pygame.init()
    # 游戏窗口
    screen = pygame.display.set_mode((480, 700))
    # bg图片
    bg_img = pygame.image.load("./images/background.png").convert_alpha()

    # 实例化我方飞机
    myplane = plane.MyPlane(bg_img.get_rect())
    #控制图片切换速度
    delay = 0
    change_img = False
    # 设置刷新速度
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
        # 频繁按键
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[K_LEFT]:
            myplane.move_left()
        elif pressedkeys[K_RIGHT]:
            myplane.move_right()
        elif pressedkeys[K_UP]:
            myplane.move_up()
        elif pressedkeys[K_DOWN]:
            myplane.move_down()
        # 画背景图片
        screen.fill((255,255,255))
        screen.blit(bg_img, bg_img.get_rect())
        if not change_img:
            screen.blit(myplane.image1, myplane.rect)
        else:
            screen.blit(myplane.image2, myplane.rect)
        delay += 1
        if delay % 5 == 0:
            change_img = True
        else:
            change_img = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()