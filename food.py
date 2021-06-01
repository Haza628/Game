import pygame
import random

class Food():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('imgs\Food.bmp')
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.y = 0.0
        self.rect.centerx = random.randint(20, 980)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def drop(self):
        self.y += 0.5
        self.rect.top = self.y
        if self.rect.top == 580:
            self.rect.top = 0
            self.y = 0.0
            self.rect.centerx = random.randint(20, 980)
