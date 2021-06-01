import sys
import pygame


def update_screen(game_setting, screen, game_character1, game_character2, food, buff):
    game_font = pygame.font.SysFont('Times New Roman', 23, True)
    screen.fill(game_setting.color)
    game_character1.blitme()
    game_character2.blitme()
    food.blitme()
    buff.blitme()
    screen.blit(game_font.render('GHZ Score:%d' % game_character1.score, True, [255, 0, 0]), [20, 20])
    screen.blit(game_font.render('YSY Score:%d' % game_character2.score, True, [255, 0, 0]), [860, 20])
    pygame.display.flip()

def update_player(game_character):
    game_character.blitme()
    pygame.display.flip()

def key(event, game_character1, game_character2):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # 右
                game_character2.move_right = True;
            if event.key == pygame.K_LEFT:  # 左
                game_character2.move_left = True;
            if event.key == pygame.K_UP and game_character2.rect.bottom == 600:  # 跳
                game_character2.move_jump = True;
            if event.key == pygame.K_d:  # 右
                game_character1.move_right = True;
            if event.key == pygame.K_a:  # 左
                game_character1.move_left = True;
            if event.key == pygame.K_w and game_character1.rect.bottom == 600:  # 跳
                game_character1.move_jump = True;
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:  # 右
                game_character2.move_right = False;
            if event.key == pygame.K_LEFT:  # 左
                game_character2.move_left = False;
            if event.key == pygame.K_d:  # 右
                game_character1.move_right = False;
            if event.key == pygame.K_a:  # 左
                game_character1.move_left = False;
            if event.key == pygame.K_w:  # 跳
                game_character1.move_jump = False;
            if event.key == pygame.K_UP:  # 跳
                game_character2.move_jump = False;


def events(game_character1, game_character2):
    # 退出语句
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        key(event, game_character1, game_character2)





