import pygame  

pygame.init()  
screen = pygame.display.set_mode((640, 480)) 
  
#load the fonts  
font = pygame.font.SysFont("Courier", 36)  

# Render the text in new surface  
text = font.render("My first Game Screen", True, (255, 16, 100))  

while True:  
	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			done = True  

	screen.fill((255, 255, 255))  

	#We will discuss blit() in the next topic  
	screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))  
	pygame.draw.rect(screen, (28,171,226), pygame.Rect(30, 30, 60, 60))
	pygame.display.flip()  