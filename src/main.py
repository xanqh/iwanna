import pygame
from game import *


def main():
    kid = Kid(enemy_shot_group, shot_se, screen)
    Enemy(shot_group, shot_se, kid)
    clock = pygame.time.Clock()
    running = True
    music_stop = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_z:
                    kid.shot()
                    # shot_se.play()

        clock.tick(60)
        screen.fill((0,0,0))
        group.update()
        if kid.gameover_flg:
            screen.blit(kid.end_text, (screen_width // 2 - 240, screen_height / 2 - 40))  # ゲームオーバー画面を表示
            if music_stop:
                pygame.mixer.music.stop()
                gameover_se.play()
                music_stop = False
        group.draw(screen)
        shot_group.update()
        shot_group.draw(screen)
        pygame.display.update()

        # print(shot_group)

    pygame.quit()

if __name__ == "__main__":
    main()