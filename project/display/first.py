'''
作者: zhangzongyan
时间: 18-4-17
'''
import pygame
import sys

# 初始化 所有的模块都初始化了 缺点:时间长  优点:免去每一个模块初始化
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
# 将窗口填充成白色
screen.fill((255,255,255))

# 设置窗口标题
pygame.display.set_caption("这是我第一个游戏窗口")

# 实例化背景图片对象  convert_alpha() 对于png使用此方法
bg = pygame.image.load("../images/bg.png").convert_alpha()

# 牛郎图片
nl_image = pygame.image.load("../images/niulang.png").convert_alpha()

# 织女图片
zv_image = pygame.image.load("../images/zhinv.png")

#牛郎运动速度
speed = [1,1]
x, y = 0, 0

clock = pygame.time.Clock()
# 循环一次就是一帧
while True:
    # 当关闭窗口 , 界面退出 ,进程终止
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 窗口关闭
            pygame.quit()
            sys.exit(0)
    # 将窗口填充成白色
    screen.fill((255, 255, 255))
    # 将背景图片加入窗口
    screen.blit(bg, bg.get_rect())
    # 画牛郎
    screen.blit(nl_image, (x, y))
    # 让牛郎移动
    if x < 0 or x > screen.get_width()-nl_image.get_width():
        speed[0] = -speed[0]
    if y < 0 or y > screen.get_height()-nl_image.get_height():
        speed[1] = -speed[1]
    x += speed[0]
    y += speed[1]

    # 画织女--->鼠标
    # 获取鼠标位置
    mouse_x, mouse_y = pygame.mouse.get_pos()
    z_x = mouse_x-zv_image.get_width() / 2
    z_y = mouse_y-zv_image.get_height() / 2
    screen.blit(zv_image, (z_x, z_y))

    # 刷新
    pygame.display.flip() # pygame.display.update()
    clock.tick(30) # 帧刷新速度






