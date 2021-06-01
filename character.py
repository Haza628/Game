import pygame
import random

class characters():
    def __init__(self, screen, img, jumpimg, x, y):
        self.screen = screen
        self.img = img
        self.jumpimg = jumpimg
        self.image = pygame.image.load(self.img)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.x = float(self.rect.left)
        self.y = float(self.rect.bottom)
        self.move_right = False
        self.move_left = False
        self.move_jump = False
        self.jump_height = 0
        self.jumptop = 150
        self.speed = 0.5
        self.score = 0


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def getfood(self, Food):
        if self.rect.left <= Food.rect.centerx:
            if self.rect.right >= Food.rect.centerx:
                if self.rect.top <= Food.rect.centery:
                    if self.rect.bottom >= Food.rect.centery:
                        Food.rect.top = 0
                        Food.y = 0.0
                        Food.rect.centerx = random.randint(20, 980)
                        self.score += 1

    def move(self):
        if self.move_right:
            self.x += self.speed
            if self.x >=970:
                self.x = 970
            self.rect.left = self.x
        if self.move_left:
            self.x -= self.speed
            if self.x <= 0:
                self.x = 0
            self.rect.left = self.x
        if self.move_jump:
            self.image = pygame.image.load(self.jumpimg)
            self.y -= self.speed
            self.jump_height += self.speed
            self.rect.bottom = self.y
            if self.jump_height >= self.jumptop:
                self.jump_height = 0
                self.move_jump = False
        else:
            self.image = pygame.image.load(self.img)
            if self.rect.bottom < 600:
                self.y += self.speed
                self.rect.bottom = self.y
            else:
                self.rect.bottom = 600

class GHZ(characters):
    def getbuff(self, buff):
        if buff.time == buff.tot_time:
            tempx = self.rect.left
            tempy = self.rect.bottom
            self.speed = 0.5
            self.img = r'imgs\GHZ.bmp'
            self.jumpimg = r'imgs\GHZ_jump.bmp'
            if self.move_jump:
                self.image = pygame.image.load(self.jumpimg)
            else:
                self.image = pygame.image.load(self.img)
            self.rect = self.image.get_rect()
            self.rect.bottom = tempy
            self.rect.left = tempx
            self.jumptop = 150
        if self.rect.left <= buff.rect.centerx:
            if self.rect.right >= buff.rect.centerx:
                if self.rect.bottom == 600:
                    buff.time = buff.nonexistent_time
                    if buff.classification == 1:
                        self.speed = 1
                        buff.rect.centerx = 5000
                    elif buff.classification == 2:
                        self.speed = 0.2
                        buff.rect.centerx = 5000
                    elif buff.classification == 3:
                        tempx = self.rect.left
                        tempy = self.rect.bottom
                        self.img = r'imgs\bigGHZ.bmp'
                        self.jumpimg = r'imgs\bigGHZ_jump.bmp'
                        if self.move_jump:
                            self.image = pygame.image.load(self.jumpimg)
                        else:
                            self.image = pygame.image.load(self.img)
                        self.rect = self.image.get_rect()
                        self.rect.bottom = tempy
                        self.rect.left = tempx
                        self.jumptop = 300
                        buff.rect.centerx = 5000

class YSY(characters):
    def getbuff(self, buff):
        if buff.time == buff.tot_time:
            tempx = self.rect.left
            tempy = self.rect.bottom
            self.speed = 0.5
            self.img = r'imgs\YSY.bmp'
            self.jumpimg = r'imgs\YSY_jump.bmp'
            if self.move_jump:
                self.image = pygame.image.load(self.jumpimg)
            else:
                self.image = pygame.image.load(self.img)
            self.rect = self.image.get_rect()
            self.rect.bottom = tempy
            self.rect.left = tempx
            self.jumptop = 150
        if self.rect.left <= buff.rect.centerx:
            if self.rect.right >= buff.rect.centerx:
                if self.rect.bottom == 600:
                    buff.time = buff.nonexistent_time
                    if buff.classification == 1:
                        self.speed = 1
                        buff.rect.centerx = 5000
                    elif buff.classification == 2:
                        self.speed = 0.2
                        buff.rect.centerx = 5000
                    elif buff.classification == 3:
                        tempx = self.rect.left
                        tempy = self.rect.bottom
                        self.img = r'imgs\bigYSY.bmp'
                        self.jumpimg = r'imgs\bigYSY_jump.bmp'
                        if self.move_jump:
                            self.image = pygame.image.load(self.jumpimg)
                        else:
                            self.image = pygame.image.load(self.img)
                        self.rect = self.image.get_rect()
                        self.rect.bottom = tempy
                        self.rect.left = tempx
                        self.jumptop = 300
                        buff.rect.centerx = 5000