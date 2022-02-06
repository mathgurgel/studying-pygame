import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') # text, AA, color

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (330, 50))

    snail_x_pos -= 4
    snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, 300))
    screen.blit(snail_surface, snail_rect)
    if snail_x_pos <= -50:
        snail_x_pos = 800
    
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)