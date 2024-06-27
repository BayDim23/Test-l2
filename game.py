import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (100, 45, 80)
BLACK = (0, 0, 0)

# Определение размеров окна игры
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Определение класса для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Ярко-красный цвет
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Определение класса для врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - 30)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - 30)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WINDOW_WIDTH - 30)

# Создание окна игры
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()