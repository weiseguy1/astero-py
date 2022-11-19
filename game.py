import pygame, sys

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30, 30), width=8, border_radius=5)

# Game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Astroids')
clock = pygame.time.Clock()

bg_surf = pygame.image.load('graphics/background.png').convert()

# ship import
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Laser
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_list = []

# Import text
font = pygame.font.Font('graphics/subatomic.ttf', 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

    # Frame rate limit
    dt = clock.tick(120) / 1000 # deltatime = px/frame / ms

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # Update position of laser
    laser_update(laser_list)
    
    # Drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf, (0, 0))

    display_score()

    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
    display_surface.blit(ship_surf, ship_rect)

    # Drawing final frame
    pygame.display.update()
