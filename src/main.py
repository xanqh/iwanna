import pygame
from game import *


def main():
    # 初期設定
    pygame.mixer.init()
    pygame.init()
    # ウィンドウの作成
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("i wanna create game with pygame!")

    game = Game()

    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_z:
                    game.kid.shot()
                if event.key == pygame.K_r and game.kid.gameover_flg:
                    game.reset()
                    # shot_se.play()

        clock.tick(60)
        screen.fill((0,0,0))
        game.run()

        # print(shot_group)

    pygame.quit()

if __name__ == "__main__":
    main()