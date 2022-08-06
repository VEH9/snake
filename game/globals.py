import pygame
from classes import SnakeBlock

pygame.init()  # Инициализировали наш объект

pygame.display.set_caption("Змейка")  # Назвали окно
frame_color = (0, 0, 255)  # Задали цвет окна в RGB
white = (255, 255, 255)  # Задаём цвет(белый) прямоугольникам в RGB
blue = (175, 238, 238)  # Задаём цвет(голубой) прямоугольникам в RGB
red = (224, 0, 0)  # Задаём цвет(красный) прямоугольникам в RGB
black = 0, 0, 0  # Задаём цвет(чёрный) для барьеров
header_color = (25, 25, 112)  # Цвет верхней части экрана
snake_color = (0, 102, 0)  # Цвет змеи
block_size = 30  # Размер прямоугольников
margin = 1  # Расстояние между клетками доски
header_margin = 70  # Расстояние по вертикали от края экрана до доски
timer = pygame.time.Clock()  # Завели таймеро, он отвечает за фпс и скорость змейки(чем больше фпс, тем больше скорость)
can_move = True  # Булевая переменная, которая используется в качестве флага для корректного передвижения
# (Чтобы мы немогли пойти в себя)
total = 0  # Счётчик съеденных яблок
font = pygame.font.SysFont('times New Roman', 36)  # Шрифт для всех надписей
speed = 1  # Устанавливаем изначальный буст к скорости
# (Скорость равна таймеру, а эту переменную мы будем прибавлять вконце в этому таймеру)
lives = 3  # Задаём кол-во жизней нашей змейке
d_row = 0  # Изменение координат по столбцу(Иксу)
d_col = 1  # Изменение координат по строке(Игрику)
this_is_a_victory = 0  # Необходимый размер змейки, чтобы победить
snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]  # Создаём змейку
bad_blocks = []  # Создаём массив барьеров, который будем заполнять в функциях
blocks_count = 21  # Кол-во прямоугольников

size = [30 * 21 + 2 * 30 + 1 * 21,  # размер окна в ширину
        30 * 21 + 2 * 30 + 1 * 21 + 71]  # Размер окна в высоту,
screen = pygame.display.set_mode(size)  # Установили размер окна


def draw_block(_color, _row, _column):
    pygame.draw.rect(screen, _color, [block_size + _column * block_size + margin * (_column + 1),
                                      header_margin + block_size + _row * block_size + margin * (_row + 1),
                                      block_size,
                                      block_size])
    # Рисуем прямоугольники (где, цвет, [координата по x, координата по y, ширина, высота])