import pygame
import random

# Initialize Pygame
pygame.

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.
BACKGROUND_COLOR_CHANGE_EVENT = pygame.

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color()
LIGHTBLUE = pygame.Color()
DARKBLUE = pygame.Color()

# Sprite colors
YELLOW = pygame.Color()
MAGENTA = pygame.Color()
ORANGE = pygame.Color()
WHITE = pygame.Color()

# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    # Constructor method
    def __init__(self, color, height, width):
        # Call to the parent class (Sprite) constructor
        super().__init__()

        # Create the sprite's surface with dimensions and color
        self.image = pygame.Surface()
        self.image.fill(color)

        # Get the sprite's rect defining its position and size
        self.rect = self.

        # Set initial velocity with random direction
        self. = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Method to update the sprite's position
    def update(self):
        # Move the sprite by its velocity
        self.rect.move_ip(self.)

        # Flag to track if the sprite hits a boundary
        boundary_hit = False

        # Check for collision with left or right boundaries and reverse direction
        if self.rect. <= 0 or self.rect. >= 500:
            self.[0] = -self.[0]
            boundary_hit = True

        # Check for collision with top or bottom boundaries and reverse direction
        if self.rect. <= 0 or self.rect. >= 400:
            self.[1] = -self.[1]
            boundary_hit = True

        # If a boundary was hit, post events to change colors
        if boundary_hit:
            pygame.event.post(pygame.event.Event())
            pygame.event.post(pygame.event.Event())

    # Method to change the sprite's color
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

# Function to change the background color
def change_background_color():
    global 
     = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()

# Instantiate the sprite
sp1 = Sprite(WHITE, )

# Randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode(())

# Set the window title
pygame.display.set_caption("Boundary Sprite")

# Set the initial background color
bg_color = BLUE

# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True

    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.()

    # If the background color change event is triggered, change the background color
    elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
      change_background_color()

  # Update all sprites
  all_sprites_list.()

  # Fill the screen with the current background color
  screen.fill(bg_color)

  # Draw all sprites to the screen
  all_sprites_list.(screen)

  # Refresh the display
  pygame.display.flip()

  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()