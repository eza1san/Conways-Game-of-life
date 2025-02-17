# Импортирование модулей
from random import randint
import pygame
from copy import deepcopy

# Задание переменных параметров поля и клеток, а также количество fps.
field_res = field_width, field_height = 1600, 900
cell = 10
cell_count_width, cell_count_height = field_width // cell, field_height // cell
fps = 30


# Запуск модуля и создание пустого окна
pygame.init()
screen = pygame.display.set_mode(field_res)
clock = pygame.time.Clock()

# Создание полей
# Следующее пустое поле(next_field)
next_field = [[0 for i in range(cell_count_width)] for j in range(cell_count_height)]

# Начальное случайное заполнение поля клетками
field = [[randint(0, 1) for i in range(cell_count_width)] for j in range(cell_count_height)]

# Различные способы заполнения поля клетками
# field = [[1 if i == cell_count_width // 2 or j == cell_count_height // 2 else 0 for i in range(cell_count_width)] for j in range(cell_count_height)]
# field = [[1 if not i % 9 else 0 for i in range(cell_count_width)] for j in range(cell_count_height)]
# field = [[1 if not (2 * i + j) % 4 else 0 for i in range(cell_count_width)] for j in range(cell_count_height)]
# field = [[1 if not (i * j) % 22 else 0 for i in range(cell_count_width)] for j in range(cell_count_height)]
# field = [[1 if not i % 7 else randint(0, 1) for i in range(cell_count_width)] for j in range(cell_count_height)]

# Создание функции определения состояния клетки
def cell_check(field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if field[j][i]:
                count += 1
    if field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

# Создание переменной для подсчета количества поколений
counter = 1

# Создание цикла while
while True:

    pygame.display.set_caption("Жизнь / Поколение " + str(counter))

    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # отрисовка сетки
    #[pygame.draw.line(screen, pygame.Color('dimgray'), (x, 0), (x, field_height)) for x in range(0, field_width, cell)]
    #[pygame.draw.line(screen, pygame.Color('dimgray'), (0, y), (field_width, y)) for y in range(0, field_height, cell)]

    # отрисовка клетки
    for x in range(1, cell_count_width -1):
        for y in range(1, cell_count_height - 1):
            if field[y][x]:
                pygame.draw.rect(screen, pygame.Color('green'), (x * cell + 2, y * cell + 2, cell -2, cell - 2))
            next_field[y][x] = cell_check(field, x, y)

    # Копирование нового поля на старую переменную
    field = deepcopy(next_field)

    counter += 1
    pygame.display.flip()
    clock.tick(fps)
