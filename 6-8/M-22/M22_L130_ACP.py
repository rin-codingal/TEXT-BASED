import pygame
import random
  
surf_color = (0, 142, 204) #background color

color1s1 = (150, 0, 150) #color 1 for sprite 1
color2s1 = (0,0,255) #color 2 for sprite 1

color1s2 = (0, 255, 0) #color 1 for sprite 2
color2s2 = (255,0,0) #color 2 for sprite 2

#position sprite 1
pos1x = random.randint(0,480)
pos1y = random.randint(0,370)

#position sprite 2
pos2x = random.randint(50,350)
pos2y = random.randint(50,300)

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
  
pygame.init()

all_sprites_list = pygame.sprite.Group()

# sprite 1 color
s1_active_color = color1s1
s1_new_color = color2s1

#sprite 2 color
s2_active_color = color1s2
s2_new_color = color2s2

# ---- new code ----
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Changing Color")
screen.fill(surf_color)

# custom user event to change color
CHANGE_COLOR = pygame.USEREVENT + 1

# posting a event to switch color after 
# every 500ms
pygame.time.set_timer(CHANGE_COLOR, 500)

# ---- new code ----

exit = True
clock = pygame.time.Clock()

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False

		# ---- new code ----
		if event.type == CHANGE_COLOR:
			#sprite 1 changing color
			if s1_active_color == s1_new_color :
				sp1 = Sprite(s1_new_color, 20, 30)
				sp1.rect.x = pos1x
				sp1.rect.y = pos1y
				all_sprites_list.add(sp1)

				s1_active_color = color1s1

			elif s1_active_color == color1s1 :
				sp1 = Sprite(color1s1, 20, 30)
				sp1.rect.x = pos1x
				sp1.rect.y = pos1y
				all_sprites_list.add(sp1)

				s1_active_color = s1_new_color
			
			#sprite 2 changing color
			if s2_active_color == s2_new_color :
				sp2 = Sprite(s2_new_color, 20, 30)
				sp2.rect.x = pos2x
				sp2.rect.y = pos2y
				all_sprites_list.add(sp2)

				s2_active_color = color1s2
			elif s2_active_color == color1s2 :
				sp2 = Sprite(color1s2, 20, 30)
				sp2.rect.x = pos2x
				sp2.rect.y = pos2y
				all_sprites_list.add(sp2)

				s2_active_color = s2_new_color
			
  
	all_sprites_list.update()
	all_sprites_list.draw(screen)

	pygame.display.update()
	clock.tick(30)

pygame.quit()
