#IMPORTS
import pygame
from pygame.locals import *
from sys import exit
import random

#SCREEN SETTINGS
size = (700, 900)
screen = pygame.display.set_mode(size)

#ENEMY CLASS
class Enemy():

    #INIT
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0

    #MOVEMENT
    def move(self):
        self.y += self.y_speed
        if self.y > 900:
            self.y = 0
            self.x = random.randint(0 , 700)
    
    #DRAW
    def draw(self):
        nuke = '/mnt/sda1/Workspace/Python/Test/nuke.png'
        boom = pygame.image.load(nuke).convert_alpha()
        screen.blit(boom, [self.x, self.y])
    
