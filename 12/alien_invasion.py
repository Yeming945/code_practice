import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)  # 设置背景色

    ship = Ship(screen)  # 创建一艘飞船

    while True:  # 开始游戏主循环
        gf.check_events(ship)  # 监视键盘和鼠标事件
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
