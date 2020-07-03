import sys
import pygame


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:  # 开始游戏主循环
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()  # 让最近绘制的屏幕可见


run_game()