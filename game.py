import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Astroids')

bg_surf = pygame.image.load('graphics/background.png').convert()

# Converts file to something pygame understands
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_y_pos = 500

font = pygame.font.Font('graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'White')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0, 0))
    ship_y_pos -= 1
    display_surface.blit(ship_surf, (300, ship_y_pos))
    display_surface.blit(text_surf, (500, 200))

    pygame.display.update()
