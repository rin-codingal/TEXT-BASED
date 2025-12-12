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

		self.image = pygame.Surface([width, height])
		self.image.fill(surf_color)
		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def moveForward(self, speed):
		self.rect.y += speed * speed/10

	def moveBack(self, speed):
		self.rect.y -= speed * speed/10

bg = pygame.image.load("L36/bg.jpeg")
bg = pygame.transform.scale(bg, ())

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("")

all_sprites_list = pygame.sprite.Group()

# Add a sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint()
sp1.rect.y = random.randint()
all_sprites_list.add(sp1)

# Add one enemy 
# set the random position
rad = 20
cxp = random.randint()
cyp = random.randint()
sp2 = Sprite((255,0,0), 20, 30)
sp2.rect.x = cxp
sp2.rect.y = cyp
all_sprites_list.add(sp2)

exit = True
clock = pygame.time.Clock()
  
while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				exit = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		sp1.moveLeft()
	if keys[pygame.K_RIGHT]:
		sp1.moveRight()
	if keys[pygame.K_DOWN]:
		sp1.moveForward()
	if keys[pygame.K_UP]:
		sp1.moveBack()

	all_sprites_list.update()
	screen.fill(surf_color)
	screen.blit(bg,(0,0))
	all_sprites_list.draw(screen)
	pygame.display.flip()

	if sp1.rect.colliderect(sp2.rect):
		all_sprites_list.remove(sp2)
		text = "You win!"

		#load the fonts  
		font = pygame.font.SysFont("Courier", 72)  
		
		# Render the text in new surface  
		text = font.render(text, True, (158, 16, 16))
		screen.blit(text,(200 - text.get_width() // 2, 140 - text.get_height() // 2))
		
		# Loading the audio
		mixer.music.load("L36/explosion.wav")
		
		# Setting the volume
		mixer.music.set_volume(0.7)
		
		# Start playing the audio
		mixer.music.play()
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()