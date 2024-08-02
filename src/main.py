import pygame
from game import *

def main():
    Kid(shot_se)
    Enemy(shot_group)
    clock = pygame.time.Clock()
    running = True

    while(running):
        clock.tick(60)
        screen.fill((0,0,0))
        bgm.set_volume(0.2)
        bgm.play(-1)
        group.update()
        group.draw(screen)
        shot_group.update()
        shot_group.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        # print(shot_group)

    pygame.quit()

if __name__ == "__main__":
    main()