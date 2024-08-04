import pygame
from game import *

def main():
    kid = Kid(shot_se)
    Enemy(shot_group, shot_se, kid)
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
                    kid.shot()
                    # shot_se.play()

        clock.tick(60)
        screen.fill((0,0,0))
        group.update()
        group.draw(screen)
        shot_group.update()
        shot_group.draw(screen)
        pygame.display.update()

        # print(shot_group)

    pygame.quit()

if __name__ == "__main__":
    main()