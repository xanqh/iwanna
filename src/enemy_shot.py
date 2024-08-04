import pygame

class Enemy_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, SE, target_x, target_y):
        super().__init__(self.containers)
        self.image = pygame.image.load("../img/shot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.SE = SE
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 1

    def shot_sound(self):
        self.SE.play()

    def update(self):
        if self.rect.x > self.target_x:
            self.rect.x -= (self.rect.x - self.target_x) / 10
        else:
            self.rect.x += (self.target_x - self.rect.x) / 10

        if self.rect.y > self.target_y:
            self.rect.y -= (self.rect.y - self.target_y) / 10
        else:
            self.rect.y += (self.target_y - self.rect.y) / 10
