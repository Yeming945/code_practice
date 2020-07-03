import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)  # 设置背景色

    ship = Ship(screen)  # 创建一艘飞船

    while True:  # 开始游戏主循环
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)  # 每次循环时都重绘屏幕
        ship.blitem()  # 放置飞船

        pygame.display.flip()  # 让最近绘制的屏幕可见


run_game()
