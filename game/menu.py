import pygame
import sys
from levels import *
import globals
from save import *

save_level = Save_Level()


def set_difficults(have_save, size):
    if not have_save:
        return [(size[0] / 3, size[1] / 2.5 - 140, u'Super easy', (250, 250, 30), (250, 30, 250), 0),
                (size[0] / 3, size[1] / 2.5 - 70, u'Easy', (250, 250, 30), (250, 30, 250), 1),
                (size[0] / 3, size[1] / 2.5, u'Medium', (250, 250, 30), (250, 30, 250), 2),
                (size[0] / 3, size[1] / 2.5 + 70, u'Hard', (250, 250, 30), (250, 30, 250), 3),
                (size[0] / 6.5, size[1] / 2.5 + 300, u'Back to Main Menu', (250, 250, 30), (250, 30, 250),
                 -1)]
    else:
        return [(size[0] / 3, size[1] / 2.5 - 140, u'Super easy', (250, 250, 30), (250, 30, 250), 0),
                (size[0] / 3, size[1] / 2.5 - 70, u'Easy', (250, 250, 30), (250, 30, 250), 1),
                (size[0] / 3, size[1] / 2.5, u'Medium', (250, 250, 30), (250, 30, 250), 2),
                (size[0] / 3, size[1] / 2.5 + 70, u'Hard', (250, 250, 30), (250, 30, 250), 3),
                (size[0] / 6.5, size[1] / 2.5 + 300, u'Back to Main Menu', (250, 250, 30), (250, 30, 250),
                 -1),
                (size[0] / 3, size[1] / 2.5 - 210, u'Continue', (250, 250, 30), (250, 30, 250), -2),
                ]


class Menu:
    def __init__(self, size=None, score=None):
        self.save = Have_save()
        self.hav_save = self.save.get()
        self.size = size
        self.str = ""
        self.punkts = [(size[0] / 2.5, size[1] / 2.5 - 70, u'Play', (250, 250, 30), (250, 30, 250), 0),
                       (size[0] / 3, size[1] / 2.5, u'Statistics', (250, 250, 30), (250, 30, 250), 1),
                       (size[0] / 2.5, size[1] / 2.5 + 70, u'Quit', (250, 250, 30), (250, 30, 250), 2)]

        self.difficults = set_difficults(self.hav_save, size)

        self.pauses = [(128, 148, u'Continue', (250, 250, 30), (250, 30, 250), 0),
                       (128, 350, u'Back to Main Menu', (250, 250, 30), (250, 30, 250), 1)]

        self.stats = [(size[0] / 5, size[1] / 2.5 - 140, 'Didicult     Score', (250, 250, 30), (250, 30, 250), 4),
                      (
                          size[0] / 5, size[1] / 2.5 - 70, f'Super easy     {score[0]}', (250, 250, 30), (250, 30, 250),
                          0),
                      (size[0] / 5, size[1] / 2.5, f'Easy              {score[1]}', (250, 250, 30), (250, 30, 250), 1),
                      (
                          size[0] / 5, size[1] / 2.5 + 70, f'Medium         {score[2]}', (250, 250, 30), (250, 30, 250),
                          2),
                      (
                          size[0] / 5, size[1] / 2.5 + 140, f'Hard              {score[3]}', (250, 250, 30),
                          (250, 30, 250),
                          3),
                      (size[0] / 6.5, size[1] / 2.5 + 300, f'Back to Main Menu', (250, 250, 30), (250, 30, 250), 5)]

    def render(self, holst, font, num_punkts, table):
        self.difficults = set_difficults(self.hav_save, self.size)
        for i in table:
            if num_punkts == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def stat(self, screen):
        done = True
        font_menu = pygame.font.SysFont('times New Roman', 70)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.stats:
                if i[0] < mp[0] < i[0] + 1055 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt, self.stats)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.pauses) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  # выбираем что делает кнопка по 5 элементу
                    if punkt == 5:
                        pygame.display.flip()
                        return
                    else:
                        continue

            pygame.display.flip()

    def menu(self, screen, lives):
        self.difficults = set_difficults(self.hav_save, self.size)
        done = True
        font_menu = pygame.font.SysFont('times New Roman', 70)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt, self.punkts)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    if lives > 0:
                        self.save.save(True)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  # выбираем что делает кнопка по 5 элементу
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        self.stat(screen)
                    elif punkt == 2:
                        sys.exit()

            pygame.display.flip()

    def choose_difficulty(self, screen):
        done = True
        font_menu = pygame.font.SysFont('times New Roman', 70)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.difficults:
                if i[0] < mp[0] < i[0] + 1055 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt, self.difficults)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.difficults) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  # выбираем что делает кнопка по 5 элементу
                    if punkt == 0:
                        return 4
                    else:
                        return punkt
            pygame.display.flip()

    def Pause(self, screen, snake_blocks):
        done = True
        font_menu = pygame.font.SysFont('times New Roman', 70)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.pauses:
                if i[0] < mp[0] < i[0] + 1055 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt, self.pauses)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.pauses) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  # выбираем что делает кнопка по 5 элементу
                    if punkt == 0:
                        return 0, snake_blocks
                    elif punkt == 1:
                        return 1, snake_blocks

            pygame.display.flip()

    @staticmethod
    def start_game(game, bad_blocks, screen):
        _done = True
        while _done:
            game.menu(screen)
            level = game.choose_difficulty(screen)
            if level == 1:
                globals.blocks_count, this_is_a_victory, bad_blocks, name = first_level(bad_blocks)
                _done = False
            elif level == 2:
                font, this_is_a_victory, globals.blocks_count, bad_blocks, name = second_level(bad_blocks)
                _done = False
            elif level == 4:
                _done = False
                globals.blocks_count, this_is_a_victory, name = easy_level()
            elif level == 3:
                font, this_is_a_victory, globals.blocks_count, bad_blocks, name = third_level(bad_blocks)
                _done = False
            elif level == -1:
                continue
            elif level == -2:
                this_is_a_victory, globals.blocks_count, bad_blocks, name = saved_level(bad_blocks)
                _done = False
