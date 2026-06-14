import pygame
import random

#initialize pygame
pygame.init()

#custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic color using pygame.Color
#background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DRAKBLUE = pygame.Color('darkblue')

#sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


#sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    #construtor method
    def __init__(self, color, height, width):
        #call to the parent class (sprite)constuctor
        super().__init__()

        #create the sprite's surface with dimension and color
        self.image = pygame.surface([width, height])
        self.image.fill(color)

        #get the sprite's rect defining it's position and size
        self.rect = self.image.get_rect()

        #set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    #method to update the sprite's position
    def update(self):
        #move the sprite by velocity
        self.rect.move_ip(self.velocity)

        #flag to track if the sprite hits a boundary
        boundary_hit = False

        #check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
                self.velocity[0] = -self.velocity[0]
                boundary_hit = True

        #check for collision with top or bottom boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 400:
                self.velocity[1] = -self.velocity[1]
                boundary_hit = True

        #if a boundary was hit, post event to change colors
        if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    #method to changethe sprite's color
    def change_color(self):
          self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


#function to change the background color
def change_background_color(self):
      global bg_color
      bg_color = random.choice([BLUE, LIGHTBLUE, DRAKBLUE])


#create a group to hold the sprite 
all_sprite_list = pygame.sprite.Group()

#instantiante the sprite
sp1 = Sprite(WHITE, 20, 30)

#randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

#add the sprite to group
all_sprite_list.add(sp1)

#create the game window
screen = pygame.display.set_mode((500, 400))

#set the window title
pygame.display.set_caption("boundery sprite")

#set the inital backgrounf color
bg_color = BLUE

#apply the background color
screen.fill(bg_color)

#game loop control flag
exit = False

#create a clock object to control frame rate
clock = pygame.time.Clock()

#main game loop
while not exit:
    # event handling loop
    for event in pygame.event.get():
        #if the window's close button is clicked , exit the game
        if event.type == pygame.QUIT:
            exit = True

        #if the sprite color change event is triggered, change sprite's color
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()

        #if the sprite color change event is triggered, change background's color
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    #update all sprites
    all_sprite_list.update

    #fill the screen with the current background color
    screen.fill(bg_color)

    #draw all sprite to the screen
    all_sprite_list.draw(screen)

    #refresh the display
    pygame.display.flip()

    #limit the frame rate to 240 fps
    clock.tick(240)

    #uninitialize all pygame modules and close the window
    pygame.quit()