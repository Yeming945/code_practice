import pygame


class Ship():
    def __init__(self, screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # 窗口大小

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # x轴是横向
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False  # 向右移动标志
        self.moving_left = False  # 向左移动标记

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitem(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
