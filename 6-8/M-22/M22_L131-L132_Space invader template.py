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
    enemyImg.append(pygame.image.load(''))
    enemyX.append(random.randint(, ))
    enemyY.append(random.randint(, ))
    enemyX_change.() #make the alien moving right automatically
    enemyY_change.() #make the alien moving down automatically

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
    score = font.render(" : " + str(score_value), True, (, , ))


def game_over_text():
    over_text = over_font.render("", True, (, , ))


def player(x, y):
    

def enemy(x, y, i):
    

def fire_bullet(x, y):
    




def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))






# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = 
            if event.key == pygame.K_RIGHT:
                playerX_change = 
            if event.key == pygame.K_SPACE:
                if bullet_state == :
                    bulletSound = mixer.Sound("")
                    bulletSound.play()

                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet()

        if event.type == pygame.KEYUP:
            if event.key == pygame. or event.key == pygame.:
                playerX_change = 

    playerX += playerX_change
    if playerX <= 0:
        
    elif playerX >= 736:
        

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 340:
            for j in range():
                enemyY[j] = 
            game_over_text()
            

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 
            enemyY[i] += enemyY_change[]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -
            enemyY[i] += enemyY_change[]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("")
            explosionSound.()
            bulletY = 
            bullet_state = 
            score_value += 
            enemyX[i] = random.randint(, )
            enemyY[i] = random.randint(, )

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        
        

    if bullet_state == "fire":
        fire_bullet(, )
        bulletY -= 

    player(, )
    show_score(, )
    pygame.display.()