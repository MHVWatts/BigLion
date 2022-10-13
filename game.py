#IMPORTS
import pygame
from pygame.locals import *
from sys import exit
import random
from nuke import Enemy

#SETTING IMAGE LOCATIONS
background_image1 = '/mnt/sda1/Workspace/Python/Test/water.jpg'
title = '/mnt/sda1/Workspace/Python/Test/title.png'
player1 = '/mnt/sda1/Workspace/Python/Test/player.png'
big_lion = '/mnt/sda1/Workspace/Python/Test/biglion.gif'
game_over = '/mnt/sda1/Workspace/Python/Test/nuke.jpg'

#SETTING COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#COUNT SCORE
count = 0

#SCREEN SETTINGS
pygame.init()
size = (700, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("you will die here")
 
#GAME SETTINGS
done = False
start_game = False
end_game = False

#LOAD PLAYER IMAGE AND ENEMY IMAGES
#Player
player = pygame.image.load(player1).convert_alpha()
x_player, y_player = 300, 700

#Big Lion
lion = pygame.image.load(big_lion).convert_alpha()
x_lion, y_lion = 200, 20

#Nukes
#Nuke 1
nuke = Enemy()
nuke.x = random.randint(0, 700)
nuke.y = 1
nuke.x_speed = 0
nuke.y_speed = 15

#Nuke 2
nuke2 = Enemy()
nuke2.x = random.randint(0, 700)
nuke2.y = 1
nuke2.x_speed = 0
nuke2.y_speed = 20

#Nuke 3
nuke3 = Enemy()
nuke3.x = random.randint(0, 700)
nuke3.y = 1
nuke3.x_speed = 0
nuke3.y_speed = 25

#Nuke 4
nuke4 = Enemy()
nuke4.x = random.randint(0, 700)
nuke4.y = 1
nuke4.x_speed = 0
nuke4.y_speed = 30

#Nuke 5
nuke5 = Enemy()
nuke5.x = random.randint(0, 700)
nuke5.y = 1
nuke5.x_speed = 0
nuke5.y_speed = 35

#MAKE MOUSE INVISIBLE
pygame.mouse.set_visible(False)

#MUSIC
pygame.mixer.init()
pygame.mixer.music.load('/mnt/sda1/Workspace/Python/Test/music.mp3')
pygame.mixer.music.play(-1)

#CLOCK
clock = pygame.time.Clock()

#MAIN LOOP
while not done:

    #EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                start_game = True

        #MOUSE POSITIONING
        pos = pygame.mouse.get_pos()
        x_player = pos[0]
        y_player = pos[1]

    #COUNT UPDATER
    if ((nuke.y == 0) or (nuke2.y == 0) or (nuke3.y == 0) or (nuke4.y == 0) or (nuke5.y == 0)):
        count += 1

    #SCREEN BOUNDARIES
    if(y_player > 840):
        y_player = 830 
    elif(y_player < 10):
        y_player = 20  
    elif(x_player > 640):
        x_player = 630  
    elif(x_player < 0):
        x_player = 10  

    #GAME GETS MORE DIFFICULT
    if count == 50:
        nuke.y_speed = 30
        nuke2.y_speed = 40
        nuke3.y_speed = 50
        nuke4.y_speed = 60
        nuke5.y_speed = 70
    if count == 100:
        nuke.y_speed = 40
        nuke2.y_speed = 60
        nuke3.y_speed = 80
        nuke4.y_speed = 100
        nuke5.y_speed = 120
    
    #COLLISION DETECTION
    #Big Lion Collision
    if (x_player + 60  >= x_lion) and (x_player + 60  <= x_lion + 300) and (y_player + 58 >= y_lion) and (y_player + 58  <= y_lion + 300):
        end_game = True

    #Nuke Collision
    if (x_player + 60  >= nuke.x) and (x_player + 60  <= nuke.x + 76) and (y_player + 58 >= nuke.y) and (y_player + 58  <= nuke.y + 108):
        end_game = True    
    if (x_player + 60  >= nuke2.x) and (x_player + 60  <= nuke2.x + 76) and (y_player + 58 >= nuke2.y) and (y_player + 58  <= nuke2.y + 108):
        end_game = True  
    if (x_player + 60  >= nuke3.x) and (x_player + 60  <= nuke3.x + 76) and (y_player + 58 >= nuke3.y) and (y_player + 58  <= nuke3.y + 108):
        end_game = True  
    if (x_player + 60  >= nuke4.x) and (x_player + 60  <= nuke4.x + 76) and (y_player + 58 >= nuke4.y) and (y_player + 58  <= nuke4.y + 108):
        end_game = True  
    if (x_player + 60  >= nuke5.x) and (x_player + 60  <= nuke5.x + 76) and (y_player + 58 >= nuke5.y) and (y_player + 58  <= nuke5.y + 108):
        end_game = True  

    #LOAD TITLE SCREEN
    #Background
    background = pygame.image.load(background_image1).convert_alpha()
    screen.blit(background, (0, 0))

    #Title
    header = pygame.image.load(title).convert_alpha()
    x_title, y_title = 7.5, 70
    screen.blit(header, (x_title, y_title))

    #Subtitle
    font = pygame.font.SysFont('Calibri', 25, True, False)
    press_space = font.render("PRESS SPACE TO CONTINUE",True, BLACK)
    screen.blit(press_space, [200, 300])
                
    #MAIN GAME START
    if start_game is True:

        #Load Background
        background = pygame.image.load(background_image1).convert_alpha()
        screen.blit(background, (0, 0))
        
        #Load Player
        screen.blit(player, (x_player, y_player))
        screen.blit(lion, (x_lion, y_lion))

        #Load Nukes
        nuke.move()
        nuke.draw()
        nuke2.move()
        nuke2.draw()
        nuke3.move()
        nuke3.draw()
        nuke4.move()
        nuke4.draw()
        nuke5.move()
        nuke5.draw()

        #Load Score
        font = pygame.font.SysFont('Calibri', 30, True, False)
        score = font.render("SCORE: " + str(count), True, BLACK)
        screen.blit(score, [550, 850])
        pygame.display.update()

        #LOAD GAME OVER SCREEN
        #Check end_game
        if end_game is True:

            #SOUND
            pygame.mixer.music.stop
            pygame.mixer.music.load('/mnt/sda1/Workspace/Python/Test/pheb.mp3')
            pygame.mixer.music.play()

            #End Loop
            while not done:

                #Quit
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                #Load End Background
                end = pygame.image.load(game_over).convert_alpha()
                screen.blit(end, (0, 0))

                #Load Game Over Message
                font = pygame.font.SysFont('Calibri', 40, True, False)
                score = font.render("GAME OVER! Your score was: " + str(count), True, BLACK)
                screen.blit(score, [100, 100])
                pygame.display.update()
                
    #UPDATE SCREEN
    pygame.display.update()
    
    #FPS
    clock.tick(144)
 
#QUIT
pygame.quit()