import pygame
import constants
from character import Character

pygame.init()


screen = pygame.display.set_mode((constants.SCREEN_WIDTH, 
    constants.SCREEN_HEIGHT))
pygame.display.set_caption("Enemies and Friends")

clock = pygame.time.Clock()

moving_left = False
moving_right = False
moving_up = False
moving_down = False

player_image = pygame.image.load(
        "assets/images/characters/elf/idle/0.png").convert_alpha()
player_image = pygame.transform.scale(player_image,
        (player_image.get_width() * constants.SCALE, 
            player_image.get_height() * constants.SCALE))

player = Character(100, 100, player_image)

run = True
while run:

    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    dx = 0
    dy = 0
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED 

    player.move(dx, dy)

    player.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()
