import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Определение класса для Змейки
class Snake:
    def init(self):
        self.body = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == "LEFT":
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + CELL_SIZE, head_y)

        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def grow(self):
        tail_x, tail_y = self.body[-1]
        if self.direction == "UP":
            new_tail = (tail_x, tail_y + CELL_SIZE)
        elif self.direction == "DOWN":
            new_tail = (tail_x, tail_y - CELL_SIZE)
        elif self.direction == "LEFT":
            new_tail = (tail_x + CELL_SIZE, tail_y)
        elif self.direction == "RIGHT":
            new_tail = (tail_x - CELL_SIZE, tail_y)

        self.body.append(new_tail)

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))


# Определение класса для Еды
class Food:
    def init(self):
        self.x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Создание окна игры
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Создание объектов Змейки и Еды
snake = Snake()
food = Food()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    snake.move()

    if snake.body[0] == (food.x, food.y):
        snake.grow()
        food = Food()

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()