import pygame
from setting import *
from enemy import Enemy
from kid import Kid
from shot import Shot

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
group = pygame.sprite.RenderUpdates()
shot_group = pygame.sprite.Group()
Enemy.containers = group
Kid.containers = group
Shot.containers = group,shot_group