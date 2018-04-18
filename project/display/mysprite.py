'''
作者: zhangzongyan
时间: 18-4-17
'''
import pygame
from pygame.locals import *

class CharactPerson(pygame.sprite.Sprite):
    def __init__(self, img_path, pos):
        pygame.sprite.Sprite.__init__(self)
        # 图片
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
        # 获取图片非透明区域
        self.mask = pygame.mask.from_surface(self.image)

def main():
    pygame.init()
    # 初始化音乐
    pygame.mixer.init()
    #加载背景音乐---->只能有一个
    bg_music = pygame.mixer.music.load("../testsounds/bg_music.ogg")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1) # 背景音乐循环播放

    # 音效 ---> 可以有多个
    win_sound = pygame.mixer.Sound("../testsounds/winner.wav")
    win_sound.set_volume(0.7)
    laugh_sound = pygame.mixer.Sound("../testsounds/laugh.wav")
    laugh_sound.set_volume(1)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("精灵是个好东西")
    bg_img = pygame.image.load("../images/bg.png").convert_alpha()

    # 牛郎--->精灵
    nl = CharactPerson("../images/niulang.png",(20, 50))
    # 创建织女精灵组
    group = pygame.sprite.Group()
    # 织女
    zv = []
    for per in range(4):
        each = CharactPerson('../images/zhinv.png', (600, per * 100))
        zv.append(each)
        # 将织女精灵加入到组内
        group.add(each)

    # 牛郎移动方向
    step = 5
    move = {K_UP:0, K_DOWN:0, K_LEFT:0, K_RIGHT:0}
    # 速度
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key in move:
                    move[event.key] = step
            if event.type == KEYUP:
                if event.key in move:
                    move[event.key] = 0
        # 画背景
        screen.fill((255,255,255))
        screen.blit(bg_img, bg_img.get_rect())
        # 牛郎的位置
        nl.rect.left += move[K_RIGHT]
        nl.rect.left -= move[K_LEFT]
        nl.rect.top += move[K_DOWN]
        nl.rect.top -= move[K_UP]
        # 画牛郎
        screen.blit(nl.image, nl.rect)

        # 画织女
        for per in zv:
            screen.blit(per.image, per.rect)

        # 检测碰撞  pygeme.sprite.collide_mask检测碰撞时只检测非透明区
        blocklist = pygame.sprite.spritecollide(nl, group, True, pygame.sprite.collide_mask)
        for b in blocklist:
            zv.remove(b)
            win_sound.play(maxtime=500)
            laugh_sound.play()

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()