'''
作者: zhangzongyan
时间: 18-4-18
'''
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, planepos):
        super().__init__()
        self.image = pygame.image.load("./images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = planepos
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 12
        self.alive = True

    def move(self):
        if self.rect.top < 0:
            self.alive = False
        else:
            self.rect.top -= self.speed
    def reset(self, planepos):
        self.rect.left, self.rect.top = planepos
        self.alive = True