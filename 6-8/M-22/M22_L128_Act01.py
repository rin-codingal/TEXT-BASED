import pygame  
  
# Setup Pygame window
pygame.init()  
screen = pygame.display.set_mode((500, 500))  
done = False  

  
while not done:
	# check the event type  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
		 
	# draw rectangle
    pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,30, 60, 60))  
  
    pygame.display.flip()  