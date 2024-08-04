import pygame
from setting import *
from enemy import Enemy
from kid import Kid
from shot import Shot
from enemy_shot import Enemy_shot

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("../msc/bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
shot_se = pygame.mixer.Sound("../msc/shot.mp3")
screen = pygame.display.set_mode((screen_width, screen_height))
group = pygame.sprite.RenderUpdates()
shot_group = pygame.sprite.Group()
Enemy.containers = group
Kid.containers = group
Shot.containers = group,shot_group
Enemy_shot.containers = group