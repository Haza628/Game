import pygame
import random

class Buff():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(r'imgs\buff.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.rect.left = random.randint(20, 960)
        self.classification = random.randint(1, 3)
        self.tot_time = 7000
        self.time = self.tot_time
        self.nonexistent_time = self.tot_time*2/5

    def blitme(self):
        if self.time > 0:
            self.time -= 1
            if self.time > self.nonexistent_time:
                self.screen.blit(self.image, self.rect)
        else:
            self.time = self.tot_time
            self.rect.left = random.randint(20, 960)
            self.classification = random.randint(1, 3)
            print(self.classification)
