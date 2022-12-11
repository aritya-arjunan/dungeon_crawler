import pygame
import constants
import math

class Character():
    def __init__(self, x, y, image):
        self.flip = False
        self.image = image
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):
        
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, canvas, facing_left, facing_down):
        flipped_image = pygame.transform.flip(self.image, facing_left,
                facing_down)
        canvas.blit(flipped_image, self.rect)
        pygame.draw.rect(canvas, constants.DARK_PURPLE, self.rect, 1)
