import pygame
import setting
import character
import function
import food
import buff

pygame.init()
pygame.font.init()
icon = pygame.image.load('imgs/icon.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption("GHZ & YSY")

game_setting = setting.Setting()
screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))

game_character1 = character.GHZ(screen, 'imgs/GHZ.bmp', 'imgs/GHZ_jump.bmp', 0, 600)
game_character2 = character.YSY(screen, 'imgs/YSY.bmp', 'imgs/YSY_jump.bmp', 970, 600)
heart = food.Food(screen)
buff = buff.Buff(screen)


while 1:
    function.update_screen(game_setting, screen, game_character1, game_character2, heart, buff)
    function.events(game_character1, game_character2)
    game_character1.move()
    game_character2.move()
    game_character1.getfood(heart)
    game_character2.getfood(heart)
    game_character1.getbuff(buff)
    game_character2.getbuff(buff)
    heart.drop()
