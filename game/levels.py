from classes import Bad_block
import globals
from save import *
from classes import SnakeBlock


def easy_level():
    snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
    globals.blocks_count = 21
    return globals.blocks_count, "Super easy", snake_blocks


def third_level(bad_blocks):  # Функция для создания первого лвла
    snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
    globals.blocks_count = 21
    bad_blocks += [Bad_block(16, 1), Bad_block(17, 1), Bad_block(18, 1), Bad_block(19, 1), Bad_block(16, 2),
                   Bad_block(17, 2), Bad_block(18, 2), Bad_block(19, 2), Bad_block(16, 3), Bad_block(17, 3),
                   Bad_block(18, 3), Bad_block(19, 3), Bad_block(16, 4), Bad_block(17, 4), Bad_block(18, 4),
                   Bad_block(19, 4), Bad_block(1, 16), Bad_block(1, 17), Bad_block(1, 18), Bad_block(1, 19),
                   Bad_block(2, 16), Bad_block(2, 17), Bad_block(2, 18), Bad_block(2, 19), Bad_block(3, 16),
                   Bad_block(3, 17), Bad_block(3, 18), Bad_block(3, 19), Bad_block(4, 16),
                   Bad_block(4, 17), Bad_block(4, 18), Bad_block(4, 19)]
    x = 1
    y = 1
    for e in range(globals.blocks_count-1):
        for i in range(4):
            for j in range(4):
                if Bad_block(x+i, y+j) not in bad_blocks and y+j != 20 and x + i != 20:
                    bad_blocks.append(Bad_block(x+i, y+j))
        x += 2
        y += 2
    return globals.blocks_count, bad_blocks, "Hard", snake_blocks


def second_level(bad_blocks):  # Функция для создания второго лвла
    snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
    globals.blocks_count = 21
    for x in range(1, 20, 2):
        for y in range(1, 20):
            bad_blocks.append(Bad_block(x, y))

    return globals.blocks_count, bad_blocks, "Medium", snake_blocks


def first_level(bad_blocks):  # Функция для создания третьего лвла
    snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
    globals.blocks_count = 21
    bad_blocks += [Bad_block(1, 1), Bad_block(1, 2), Bad_block(1, 3), Bad_block(2, 1), Bad_block(2, 2), Bad_block(2, 3),
                   Bad_block(3, 1), Bad_block(3, 2), Bad_block(3, 3),
                   Bad_block(17, 1), Bad_block(17, 2), Bad_block(17, 3), Bad_block(18, 1), Bad_block(18, 2),
                   Bad_block(18, 3),
                   Bad_block(19, 1), Bad_block(19, 2), Bad_block(19, 3), Bad_block(1, 17), Bad_block(2, 17),
                   Bad_block(3, 17), Bad_block(1, 18), Bad_block(2, 18), Bad_block(3, 18),
                   Bad_block(1, 19), Bad_block(2, 19), Bad_block(3, 19),
                   Bad_block(17, 17), Bad_block(17, 18), Bad_block(17, 19), Bad_block(18, 17), Bad_block(18, 18),
                   Bad_block(18, 19),
                   Bad_block(19, 17), Bad_block(19, 18), Bad_block(19, 19)]
    for i in range(globals.blocks_count):
        for j in range(globals.blocks_count):
            if (i == 10 and 3 < j < 17) or (j == 10 and 3 < i < 17):
                bad_blocks.append(Bad_block(i, j))
    return globals.blocks_count, bad_blocks, "Easy", snake_blocks


def saved_level(bad_blocks):
    save_level = Save_Level()
    globals.blocks_count = save_level.get('blocks_count')
    bad_blocks += save_level.get('bad_blocks')
    name = save_level.get('name')
    _done = False
    snake_blocks = save_level.get('snake_blocks')

    return globals.blocks_count, bad_blocks, name, snake_blocks
