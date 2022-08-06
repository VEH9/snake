import sys
import random

from levels import *
from menu import Menu
from globals import *
from save import *


def get_random_entry_block():  # Функция для вычисления рандомного блока для спавна яблока
    x = random.randint(1, globals.blocks_count - 1)
    y = random.randint(1, globals.blocks_count - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks or Bad_block(x, y) in bad_blocks:
        x = random.randint(1, globals.blocks_count - 1)
        y = random.randint(1, globals.blocks_count - 1)
        empty_block = SnakeBlock(x, y)
    return empty_block


name = ""
total = globals.total
speed = globals.speed
snake_blocks = globals.snake_blocks
d_row = globals.d_row
can_move = globals.can_move
d_col = globals.d_col
apple = get_random_entry_block()
snake_blocks_saved = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
d_col_saved = globals.d_col
d_row_saved = globals.d_row
save = Save()
score = [save.get("Super easy"), save.get("Easy"), save.get("Medium"), save.get("Hard")]
game = Menu(size, score)
lives = 0
save_level = Save_Level()
have_save = Have_save()
bad_blocks = globals.bad_blocks
_done = True
continue_game = False
while _done:
    game.menu(screen, lives)
    level = game.choose_difficulty(screen)
    if level == 1:
        globals.blocks_count, bad_blocks, name, snake_blocks = first_level(bad_blocks)
        _done = False
    elif level == 2:
        globals.blocks_count, bad_blocks, name, snake_blocks = second_level(bad_blocks)
        _done = False
    elif level == 4:
        _done = False
        globals.blocks_count, name, snake_blocks = easy_level()
    elif level == 3:
        globals.blocks_count, bad_blocks, name, snake_blocks = third_level(bad_blocks)
        _done = False
    elif level == -1:
        continue
    elif level == -2:
        globals.blocks_count, bad_blocks, name, snake_blocks = saved_level(bad_blocks)
        total = save_level.get('total')
        speed = save_level.get('speed')
        lives = save_level.get('lives')
        d_row = save_level.get('d_row')
        can_move = save_level.get('can_move')
        d_col = save_level.get('d_col')
        continue_game = True
        apple = save_level.get('apple')
        _done = False

font = globals.font
if not continue_game:
    total = globals.total
    speed = globals.speed
    lives = globals.lives
    snake_blocks = globals.snake_blocks
    d_row = globals.d_row
    can_move = globals.can_move
    d_col = globals.d_col
    apple = get_random_entry_block()

while True:  # Бесконечный цикл в котором всё происходит
    # region рисуем
    screen.fill(frame_color)  # Заполнили экран цветом
    pygame.draw.rect(screen, header_color, [0, 0, size[0], header_margin])  # Нарисовали верхнюю часть экрана
    # (где, цвет, [координата по x, координата по y, ширина, высота])

    text_total = font.render(f"Total: {total}", False, white)  # Создание нужного нам текста
    text_speed = font.render(f"Speed: {speed}", False, white)
    text_lives = font.render(f"Lives: {lives}", False, white)
    screen.blit(text_total, (block_size, block_size))  # Вывод на экран нашего текста
    screen.blit(text_lives, (blocks_count * block_size // 2, block_size))
    screen.blit(text_speed, (block_size * blocks_count - text_speed.get_size()[0] // 1.6, block_size))
    # (текст сообщения, (координата по y, координата по x,)), во втором случае они такие, чтобы всё хорошо
    # отображаллось, при изменение кол-ва плиток или размера окна
    # Запусти, посмотри, тотал - слева, скорость - справа
    for row in range(globals.blocks_count):
        for column in range(globals.blocks_count):
            if Bad_block(row, column) in bad_blocks:
                color = black
            elif (row + column) % 2 == 0:
                color = blue
            else:
                color = white
            draw_block(color, row, column)  # Рисуем прямоугольники: где, каким цветом, начальные координаты и размер
            # Алгоритм как у рисовки шахматной доски

    draw_block(red, apple.x, apple.y)  # Рисуем яблочко

    for blocks in snake_blocks:  # Рисуем змейку
        draw_block(snake_color, blocks.x, blocks.y)
    # endregion
    pygame.display.flip()  # Применяет всё то, что мы написали, выводит всё на экран на экран
    # (Сетку, змейку, яблоко, текст и т.д.)
    head = snake_blocks[-1]  # Создаём переменную, в которой будем хранить голову змеи

    for event in pygame.event.get():  # Обрабатываем все действия пользователя
        if event.type == pygame.QUIT:  # Если нажали на "Esc", то игра закрывается
            if lives > 0:
                have_save.save(True)
                save_level.save(blocks_count, bad_blocks, name, total, lives, snake_blocks, apple, speed,
                                d_row, d_col, can_move)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Обрабатываем нажатия с клавишь и
            # соотвественно перемещаем голову змеи(управление стрелками)
            if event.key == pygame.K_UP and d_col != 0 and can_move:
                d_row = -1
                d_col = 0
                can_move = False
            elif event.key == pygame.K_DOWN and d_col != 0 and can_move:
                d_row = 1
                d_col = 0
                can_move = False
            elif event.key == pygame.K_LEFT and d_row != 0 and can_move:
                d_row = 0
                d_col = -1
                can_move = False
            elif event.key == pygame.K_RIGHT and d_row != 0 and can_move:
                d_row = 0
                d_col = 1
                can_move = False
            elif event.key == pygame.K_r:  # Пасхалка, если нажать R, то все барьеры пропадут
                bad_blocks.clear()
            elif event.key == pygame.K_e:  # Пасхалка, если нажать e, то яблоко заспаниться прямо перед змейкой
                apple = SnakeBlock(snake_blocks[-1].x + d_row, snake_blocks[-1].y + d_col)
            elif event.key == pygame.K_ESCAPE:
                timer.tick(0)
                save_level.save(blocks_count, bad_blocks, name, total, lives, snake_blocks, apple, speed,
                                d_row, d_col, can_move)
                have_save.save(True)
                action, snake_blocks = game.Pause(screen, snake_blocks)

                if action == 0:
                    timer.tick(3 + speed)
                if action == 1:

                    snake_blocks_saved = snake_blocks
                    d_col_saved = d_col
                    d_row_saved = d_row
                    bad_blocks.clear()
                    lives = 3
                    speed = 1
                    total = 0
                    done = True
                    while done:
                        game = Menu(size, score)
                        game.menu(screen, lives)
                        level = game.choose_difficulty(screen)
                        if level != -2:
                            snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
                            new_head = head = snake_blocks[-1]
                            d_row = 0  # Изменение координат по столбцу(Иксу)
                            d_col = 1  # Изменение координат по строке(Игрику)
                            delete_save(have_save, save_level)
                        if level == 1:
                            globals.blocks_count, bad_blocks, name, snake_blocks = first_level(bad_blocks)
                            done = False
                            apple = get_random_entry_block()
                        elif level == 2:
                            globals.blocks_count, bad_blocks, name, snake_blocks = second_level(bad_blocks)
                            done = False
                            apple = get_random_entry_block()
                        elif level == 4:
                            globals.blocks_count, name, snake_blocks = easy_level()
                            done = False
                            apple = get_random_entry_block()
                        elif level == 3:
                            globals.blocks_count, bad_blocks, name, snake_blocks = third_level(bad_blocks)
                            apple = get_random_entry_block()
                            done = False
                        elif level == -1:
                            continue
                        elif level == -2:
                            try:
                                d_row = save_level.get('d_row')
                                d_col = save_level.get('d_col')
                                globals.blocks_count, bad_blocks, name, snake_blocks = saved_level(bad_blocks)
                            except Exception:
                                d_row = d_row_saved
                                d_col = d_col_saved
                                snake_blocks = snake_blocks_saved
                            total = save_level.get('total')
                            speed = save_level.get('speed')
                            lives = save_level.get('lives')
                            can_move = save_level.get('can_move')
                            continue_game = True
                            apple = save_level.get('apple')
                            done = False
                    pygame.display.flip()

    if not head.is_inside(globals.blocks_count) or Bad_block(head.x,
                                                             head.y) in bad_blocks:  # Если врезаемся в стену, то
        # всё, гг
        if name == "Super easy" and total > score[0]:
            save.save(name, total)
            score[0] = total
        if name == "Easy" and total > score[1]:
            save.save(name, total)
            score[1] = total
        if name == "Medium" and total > score[2]:
            save.save(name, total)
            score[2] = total
        if name == "Hard" and total > score[3]:
            save.save(name, total)
            score[3] = total
        delete_save(have_save, save_level)
        game = Menu(size, score)
        bad_blocks.clear()
        lives = 3
        speed = 1
        total = 0
        done = True
        while done:
            game.menu(screen, lives)
            level = game.choose_difficulty(screen)
            d_row = 0  # Изменение координат по столбцу(Иксу)
            d_col = 1  # Изменение координат по строке(Игрику)
            snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
            head = snake_blocks[-1]
            if level == 1:
                globals.blocks_count, bad_blocks, name, snake_blocks = first_level(bad_blocks)
                done = False
                apple = get_random_entry_block()
            elif level == 2:
                globals.blocks_count, bad_blocks, name, snake_blocks = second_level(bad_blocks)
                done = False
                apple = get_random_entry_block()
            elif level == 4:
                globals.blocks_count, name, snake_blocks = easy_level()
                done = False
                apple = get_random_entry_block()
            elif level == 3:
                globals.blocks_count, bad_blocks, name, snake_blocks = third_level(bad_blocks)
                apple = get_random_entry_block()
                done = False
            elif level == -1:
                continue
        pygame.display.flip()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)  # Вычисляем новое значение головы(Тоже в гс объясню)
    can_move = True
    if new_head in snake_blocks:  # Если врезаемся в себя, то всё, гг
        if lives:
            lives -= 1
            have_save.save(True)
        else:
            if name == "Super easy" and total > score[0]:
                save.save(name, total)
                score[0] = total
                delete_save(have_save, save_level)
            if name == "Easy" and total > score[1]:
                save.save(name, total)
                score[1] = total
                delete_save(have_save, save_level)
            if name == "Medium" and total > score[2]:
                save.save(name, total)
                score[2] = total
                have_save.save(False)
            if name == "Hard" and total > score[3]:
                save.save(name, total)
                score[3] = total
                delete_save(have_save, save_level)

            game = Menu(size, score)
            bad_blocks.clear()
            lives = 3
            speed = 1
            total = 0
            done = True
            while done:
                game.menu(screen, lives)
                level = game.choose_difficulty(screen)
                if level != -2:
                    snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
                    new_head = head = snake_blocks[-1]
                    d_row = 0  # Изменение координат по столбцу(Иксу)
                    d_col = 1  # Изменение координат по строке(Игрику)
                    delete_save(have_save, save_level)
                if level == 1:
                    globals.blocks_count, bad_blocks, name = first_level(bad_blocks)
                    done = False
                    apple = get_random_entry_block()
                elif level == 2:
                    globals.blocks_count, bad_blocks, name = second_level(bad_blocks)
                    done = False
                    apple = get_random_entry_block()
                elif level == 4:
                    globals.blocks_count, name = easy_level()
                    done = False
                    apple = get_random_entry_block()
                elif level == 3:
                    globals.blocks_count, bad_blocks, name = third_level(bad_blocks)
                    apple = get_random_entry_block()
                    done = False
                elif level == -1:
                    continue
                elif level == -2:
                    try:
                        d_row = save_level.get('d_row')
                        d_col = save_level.get('d_col')
                        globals.blocks_count, bad_blocks, name, snake_blocks = saved_level(bad_blocks)
                    except Exception:
                        snake_blocks = snake_blocks_saved
                        d_row = d_row_saved
                        d_col = d_col_saved
                    total = save_level.get('total')
                    speed = save_level.get('speed')
                    lives = save_level.get('lives')
                    can_move = save_level.get('can_move')
                    continue_game = True
                    done = False

            pygame.display.flip()
    # region яблоки и рост
    if apple == head:  # Если мы скушали яблочко
        total += 1  # Прибавляем 1 к счетчику
        speed = total // 5 + 1  # За каждые 5 съеденных яблок, скорость увеличивается на 1
        snake_blocks.append(apple)  # Добовляем блок съеденного яблока к нашей змейки
        apple = get_random_entry_block()  # Вычисляем новое расположение яблока
    else:
        snake_blocks.pop(0)  # Тоже запишу голосовое, объясню как работает наша змейка

    snake_blocks.append(new_head)  # Добавляем новое значение головы к нашей змейки

    timer.tick(3 + speed)  # Увеличиваем скорость
    # endregion
