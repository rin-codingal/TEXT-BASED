import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load("")

# Sound
mixer.music.load("")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("")
playerX = 
playerY = 
playerX_change = 

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 

for i in range(num_of_enemies):
    

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load("")
bulletX = 
bulletY = 
bulletX_change = 
bulletY_change = 
bullet_state = 

# Score
score_value = 
font = pygame.font.Font()

textX = 
testY = 

# Game Over
over_font = pygame.font.Font()


def show_score(x, y):
    


def game_over_text():
    


def player(x, y):
    


def enemy(x, y, i):
    


def fire_bullet(x, y):
    


def isCollision(enemyX, enemyY, bulletX, bulletY):
    


# Game Loop


while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            

        if event.type == pygame.KEYUP:
            

    playerX += playerX_change
    if playerX <= 0:
        
    elif playerX >= 736:
        

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 340:
            

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            
        elif enemyX[i] >= 736:
            

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    