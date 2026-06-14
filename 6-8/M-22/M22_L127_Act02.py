import pygame  

# Initialize required modules
pygame.init()  
white = (255, 255, 255)
screen_width, screen_height = 500, 500

# Clock
clock = pygame.time.Clock()
  
# creating the display surface object of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((screen_width, screen_height))  
  
# set the pygame window name   
pygame.display.set_caption('Add Image to The Window')  
  
# load and scale image
bg_image = pygame.transform.scale(pygame.image.load('L33/bg-cartoon.jpg').convert(), (screen_width, screen_height))   

image = pygame.image.load('L33/turtle.jpeg')  

text = pygame.font.Font(None, 36).render("Hello", True, pygame.Color('black'))

# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)
  
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Set a default position
DEFAULT_IMAGE_POSITION = (150,150)

# infinite loop   
while True:  
	display_surface.fill(white)  
	display_surface.blit(bg_image, (0, 0))
	display_surface.blit(image, DEFAULT_IMAGE_POSITION)  
	display_surface.blit(text, DEFAULT_IMAGE_POSITION)

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			pygame.quit()  
			# quit the program.   
			quit()  
		
	# Part of event loop
	pygame.display.flip()
	clock.tick(30)