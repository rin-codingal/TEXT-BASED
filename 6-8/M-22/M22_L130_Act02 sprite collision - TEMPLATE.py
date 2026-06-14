#Level up this game
import pygame
import random
from pygame import mixer
  
# Starting the mixer
mixer.init()  
  
surf_color = ()
color = (0, 0, 0)

# Object class
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([])
		self.image.fill(surf_color)
		pygame.draw.rect(self.image,color,pygame.)
		self.rect = self.image.get_rect()

	def moveRight(self, ):
		self.rect.x += 

	def moveLeft(self, ):
		self.rect.x -= 

	def moveForward():
		self.rect.y += 

	def moveBack():
		self.rect.y -= 

bg = pygame.image.load("")
bg = pygame.transform.

pygame.init()

screen = pygame.display.set_mode((, ))
pygame.display.set_caption("")

all_sprites_list = pygame.sprite.

# Add a sprite
sp1 = Sprite()
sp1.rect.x = random.()
sp1.rect.y = random.()
all_sprites_list.add()

# Add one enemy 
# set the random position
rad = 20
cxp = random.randint()
cyp = random.randint()
sp2 = Sprite((255,0,0), , )
sp2.rect.x = 
sp2.rect.y = 
all_sprites_list.add()

exit = True
clock = pygame.time.()
  
while exit:
	for event in pygame.event.():
		if event.type == pygame.:
			exit = False
		elif event.type == pygame.:
			if event.key == pygame.K_x:
				exit = False

	keys = pygame.key.get_pressed()
	if keys[pygame.]:
		sp1.()
	if keys[pygame.]:
		sp1.()
	if keys[pygame.]:
		sp1.()
	if keys[pygame.]:
		sp1.()

	all_sprites_list.update()
	screen.fill()
	screen.blit(bg,(0,0))
	all_sprites_list.
	pygame.display.flip()

	if sp1.rect.colliderect(sp2.):
		all_sprites_list.
		text = "You win!"

		#load the fonts  
		font = pygame.font.SysFont("Courier", 72)  
		
		# Render the text in new surface  
		text = font.render(text, True, (158, 16, 16))
		screen.blit(text,(200 - text.() // 2, 140 - text.() // 2))
		
		# Loading the audio
		mixer.music.load("")
		
		# Setting the volume
		mixer.music.set_volume()
		
		# Start playing the audio
		mixer.music.play()
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()