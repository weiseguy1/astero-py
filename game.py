import pygame
import sys

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups) # Init the parent class
        self.image = pygame.image.load('graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)



pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Astroids')
clock = pygame.time.Clock()

# Background
background_surf = pygame.image.load("graphics/background.png")


# shrite group
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser((100, 300), laser_group)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # background
    display_surf.blit(background_surf, (0, 0))

    # graphics
    spaceship_group.draw(display_surf)
    laser_group.draw(display_surf)

    # draw the frame
    pygame.display.update()
