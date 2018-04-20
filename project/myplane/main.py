'''
作者: zhangzongyan
时间: 18-4-18
'''
import pygame
from pygame.locals import  *
import plane
import enemy

SMALL_ENEMY_NUM = 15
MID_ENEMY_NUM = 10
BIG_ENEMY_NUM = 5

# 将敌机加入组中
def add_group(group1, group2, eny):
    group1.add(eny)
    group2.add(eny)

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

    # 敌机组
    enemies_group = pygame.sprite.Group()
    # 小敌机组
    smallEny_group = pygame.sprite.Group()
    # 实例化小型机-->15个
    for i in range(SMALL_ENEMY_NUM):
        small = enemy.SmallEnemy(bg_img.get_rect())
        add_group(enemies_group, smallEny_group, small)
    # 中敌机组
    midEny_group = pygame.sprite.Group()
    for i in range(MID_ENEMY_NUM):
        small = enemy.MidEnemy(bg_img.get_rect())
        add_group(enemies_group, midEny_group, small)

    # 大敌机组
    bigEny_group = pygame.sprite.Group()
    for i in range(BIG_ENEMY_NUM):
        small = enemy.BigEnemy(bg_img.get_rect())
        add_group(enemies_group, bigEny_group, small)

    # 销毁索引
    small_index = 0
    mid_index = 0
    big_index = 0
    me_index = 0

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

        # 绘制敌机
        for e in bigEny_group:
            if e.alive:
                e.move()
                if delay % 4 == 0:
                    screen.blit(e.image1, e.rect)
                else:
                    screen.blit(e.image2, e.rect)
            else:
                screen.blit(e.destroy_image[big_index], e.rect)
                if delay % 3 == 0:
                    big_index += 1
                    if big_index == 6:
                        big_index = 0
                        e.reset()

        for e in midEny_group:
            if e.alive:
                e.move()
                screen.blit(e.image, e.rect)
            else:
                screen.blit(e.destroy_image[mid_index], e.rect)
                if delay % 3 == 0:
                    mid_index += 1
                    if mid_index == 4:
                        mid_index = 0
                        e.reset()
        for e in smallEny_group:
            if e.alive:
                e.move()
                screen.blit(e.image, e.rect)
            else:
                e.reset()

        # 检测敌机是否撞击我方飞机
        collide_plane = pygame.sprite.spritecollide(myplane, enemies_group, False, \
                                    pygame.sprite.collide_mask)
        if collide_plane:
            # 发生碰撞
            for e in collide_plane:
                e.alive = False
                #myplane.alive = False

        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1, myplane.rect)
            else:
                screen.blit(myplane.image2, myplane.rect)
        else:
            running = False
        delay += 1
        if delay % 5 == 0:
            change_img = True
        else:
            change_img = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()