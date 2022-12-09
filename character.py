import pygame
import constants

class Character():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, canvas):
        pygame.draw.rect(canvas, constants.DARK_PURPLE, self.rect)
