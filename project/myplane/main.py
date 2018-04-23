'''
作者: zhangzongyan
时间: 18-4-18
'''
import pygame
from pygame.locals import  *
import plane
import enemy
import bullet

SMALL_ENEMY_NUM = 15
MID_ENEMY_NUM = 10
BIG_ENEMY_NUM = 5
BULLET_NUM = 5

# 创建指定个数的小型敌机 并加入组内
def add_small_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemy.SmallEnemy(bg_rect)
        group1.add(each)
        group2.add(each)

# 创建指定个数的中型敌机 并加入组内
def add_mid_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemy.MidEnemy(bg_rect)
        group1.add(each)
        group2.add(each)

# 创建指定个数的大型敌机 并加入组内
def add_big_enemy(group1, group2, num, bg_rect):
    for i  in range(num):
        each = enemy.BigEnemy(bg_rect)
        group1.add(each)
        group2.add(each)

# 改变敌机组内敌机速度
def speed_increace(group, inc):
    for e in group:
        e.speed += inc
def main():
    # 初始化游戏
    pygame.init()
    # 游戏窗口
    screen = pygame.display.set_mode((480, 700))
    # bg图片
    bg_img = pygame.image.load("./images/background.png").convert_alpha()

    # 回去背景的宽度和高度
    width = bg_img.get_rect().width
    height = bg_img.get_rect().height

    # 标题
    pygame.display.set_caption("飞机大战--Bata")

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
    add_small_enemy(smallEny_group, enemies_group, SMALL_ENEMY_NUM, bg_img.get_rect())

    # 中敌机组
    midEny_group = pygame.sprite.Group()
    add_mid_enemy(midEny_group, enemies_group, MID_ENEMY_NUM, bg_img.get_rect())

    # 大敌机组
    bigEny_group = pygame.sprite.Group()
    add_big_enemy(bigEny_group, enemies_group, BIG_ENEMY_NUM, bg_img.get_rect())

    # 销毁索引
    mid_index = 0
    big_index = 0
    me_index = 0
    bullet_index = 0

    print(myplane.rect.width)
    print(myplane.rect.midtop)

    # 实例化子弹对象
    bullet_group = pygame.sprite.Group()
    bulletlist = []
    for i in range(BULLET_NUM):
        b = bullet.Bullet(myplane.rect.midtop)
        bullet_group.add(b)
        bulletlist.append(b)

    # 设置刷新速度
    clock = pygame.time.Clock()

    # 显示分数
    score = 0
    # font对象
    fnt = pygame.font.Font('./font/myfont.ttf', 24)

    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.play(-1)

    # 暂停播放按钮
    pause_nor_img = pygame.image.load("./images/pause_nor.png")
    pause_pressed_img = pygame.image.load("./images/pause_pressed.png")
    resume_nor_img = pygame.image.load("./images/resume_nor.png")
    resume_pressed_img = pygame.image.load("./images/resume_pressed.png")
    pause_img = pause_nor_img
    pause_rect = pause_img.get_rect()
    pause_rect.left, pause_rect.top = (width-pause_rect.width -5, 5)
    pause_flag = False

    # 等级
    level = 1

    # 炸弹
    bomb_img = pygame.image.load("./images/bomb.png").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_rect.left, bomb_rect.top = (5, height-bomb_rect.height-5)
    bom_num = 3
    fnt2 = pygame.font.Font('./font/myfont.ttf', 48)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
            elif event.type == MOUSEBUTTONDOWN:
                # 点击鼠标左键 并在按钮区域
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                   pause_flag = not pause_flag
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if pause_flag:
                        # 暂停
                        pause_img = resume_pressed_img
                    else:
                        pause_img = pause_pressed_img
                else:
                    if pause_flag:
                        pause_img = resume_nor_img
                    else:
                        pause_img = pause_nor_img
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # 放炸弹
                    for e in enemies_group:
                        if e.alive and e.rect.top > 0:
                            e.alive = False
                    bom_num -= 1

        # 画背景图片
        screen.fill((255, 255, 255))
        screen.blit(bg_img, bg_img.get_rect())
        if not pause_flag:
            # 判断等级
            if level == 1 and score > 50000:
                level = 2
                # 多5个小敌机 2中敌机 1大敌机
                add_small_enemy(smallEny_group, enemies_group, 5, bg_img.get_rect())
                add_mid_enemy(midEny_group, enemies_group, 2, bg_img.get_rect())
                add_big_enemy(bigEny_group, enemies_group, 1, bg_img.get_rect())
                # 小敌机速度+2 中敌机速度加1
                speed_increace(smallEny_group, 2)
                speed_increace(midEny_group, 1)
            elif level == 2 and score > 150000:
                level = 3
                # 多5个小敌机 2中敌机 1大敌机
                add_small_enemy(smallEny_group, enemies_group, 10, bg_img.get_rect())
                add_mid_enemy(midEny_group, enemies_group, 5, bg_img.get_rect())
                add_big_enemy(bigEny_group, enemies_group, 2, bg_img.get_rect())
                # 小敌机速度+2 中敌机速度加1
                speed_increace(smallEny_group, 3)
                speed_increace(midEny_group, 2)

            # 频繁按键
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[K_LEFT] or pressedkeys[K_a]:
                myplane.move_left()
            elif pressedkeys[K_RIGHT] or pressedkeys[K_d]:
                myplane.move_right()
            elif pressedkeys[K_UP] or pressedkeys[K_w]:
                myplane.move_up()
            elif pressedkeys[K_DOWN] or pressedkeys[K_s]:
                myplane.move_down()

            # 子弹重置
            if not delay % 10:
                bulletlist[bullet_index].reset(myplane.rect.midtop)
                bullet_index = (bullet_index + 1) % BULLET_NUM

            # 绘制子弹
            for d in bullet_group:
                if d.alive:
                    d.move()
                    screen.blit(d.image, d.rect)
                    # 子弹是否与敌机发生碰撞
                    colleny = pygame.sprite.spritecollide(d, enemies_group, False, pygame.sprite.collide_mask)
                    for e in colleny:
                        if e in smallEny_group:
                            score += 1000
                            e.alive = False
                        else:
                            e.energy -= 1
                            if e.energy == 0:
                                if e in bigEny_group:
                                    score += 10000
                                else:
                                    score += 5000
                                e.alive = False
                        d.alive = False

            # 绘制敌机
            for e in bigEny_group:
                if e.alive:
                    e.move()
                    if delay % 4 == 0:
                        screen.blit(e.image1, e.rect)
                    else:
                        screen.blit(e.image2, e.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, (0,0,0), (e.rect.left, e.rect.top-5), \
                                     (e.rect.right, e.rect.top-5), 2)
                    # 余血
                    current_egy = e.energy / enemy.BigEnemy.energy
                    if current_egy < 0.2:
                        color_paint = (255, 0, 0)
                    else:
                        color_paint = (0, 255, 0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)

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
                    # 绘制血槽
                    pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                     (e.rect.right, e.rect.top - 5), 2)
                    # 余血
                    current_egy = e.energy / enemy.MidEnemy.energy
                    if current_egy < 0.2:
                        color_paint = (255,0,0)
                    else:
                        color_paint = (0,255,0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left+e.rect.width * current_egy, e.rect.top - 5), 2)
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

        myrender = fnt.render("Score:%d" % score, True, (234, 222, 56))
        # 显示文字
        screen.blit(myrender, (5, 5))

        # 显示等级
        myrender = fnt.render("Level:%d" % level, True, (234,222,56))
        screen.blit(myrender, (width-myrender.get_rect().width-5, height-myrender.get_rect().height-5))

        # 显示炸弹
        if bom_num > 0:
            screen.blit(bomb_img, bomb_rect)
            myrender = fnt2.render("x %d" % bom_num, True, (234,222,56))
            screen.blit(myrender, (bomb_rect.right+2, bomb_rect.top))

        if myplane.alive:
            if not change_img:
                screen.blit(myplane.image1, myplane.rect)
            else:
                screen.blit(myplane.image2, myplane.rect)
        else:
            # 销毁
            screen.blit(myplane.destroy_images[me_index], myplane.rect)
            if not delay % 10:
                me_index += 1
                if me_index == 4:
                    running = False

        # 绘制暂停开始
        screen.blit(pause_img, pause_rect)

        delay += 1
        if delay % 5 == 0:
            change_img = True
        else:
            change_img = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()