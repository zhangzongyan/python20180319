'''
作者: zhangzongyan
时间: 18-4-18
'''
import pygame
import random

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 小敌机图片--->Surface
        self.image = pygame.image.load("./images/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy1_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy1_down4.png").convert_alpha()]

        # 背景的宽度, 高度
        self.width = bg_size.width
        self.height = bg_size.height

        # 位置
        self.rect.left, self.rect.top = (random.randint(0, self.width-self.rect.width),\
                                         random.randint(-5*self.height, 0))
        # 速度
        self.speed = 2
        # 非透明区
        self.mask = pygame.mask.from_surface(self.image)
        # 状态
        self.alive = True
    # 移动
    def move(self):
        if self.rect.top >= self.height-self.rect.height-50:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                            random.randint(-5 * self.height, 0))

class MidEnemy(pygame.sprite.Sprite):
    energy = 10
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 小敌机图片--->Surface
        self.image = pygame.image.load("./images/enemy2.png")
        self.rect = self.image.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy2_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy2_down4.png").convert_alpha()]

        # 背景的宽度, 高度
        self.width = bg_size.width
        self.height = bg_size.height

        # 实例能量
        self.energy = MidEnemy.energy
        # 位置
        self.rect.left, self.rect.top = (random.randint(0, self.width-self.rect.width),\
                                         random.randint(-10*self.height, -5 * self.height))
        # 速度
        self.speed = 1
        # 非透明区
        self.mask = pygame.mask.from_surface(self.image)
        # 状态
        self.alive = True
    # 移动
    def move(self):
        if self.rect.top >= self.height-self.rect.height-50:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-10 * self.height, -5 * self.height))
        self.energy = MidEnemy.energy


class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 小敌机图片--->Surface
        self.image1 = pygame.image.load("./images/enemy3_n1.png")
        self.image2 = pygame.image.load("./images/enemy3_n2.png")
        self.rect = self.image1.get_rect()
        # 撞击图片
        self.destroy_image = [pygame.image.load("./images/enemy3_down1.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down2.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down3.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down4.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down5.png").convert_alpha(), \
                              pygame.image.load("./images/enemy3_down6.png").convert_alpha(),]

        # 背景的宽度, 高度
        self.width = bg_size.width
        self.height = bg_size.height

        self.energy = BigEnemy.energy

        # 位置
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15 * self.height, -10*self.height))
        # 速度
        self.speed = 1
        # 非透明区
        self.mask = pygame.mask.from_surface(self.image1)
        # 状态
        self.alive = True

    # 移动
    def move(self):
        if self.rect.top >= self.height - self.rect.height - 50:
            self.reset()
        else:
            self.rect.top += self.speed

    def reset(self):
        self.alive = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width), \
                                         random.randint(-15 * self.height, -10*self.height))
        self.energy = BigEnemy.energy

