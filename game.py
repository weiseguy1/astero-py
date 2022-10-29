import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Astroids')

bg_surf = pygame.image.load('graphics/background.png').convert()

# Converts file to something pygame understands
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((200, 200, 200))
    display_surface.blit(bg_surf, (0, 0))
    display_surface.blit(ship_surf, (300, 500))

    pygame.display.update()
