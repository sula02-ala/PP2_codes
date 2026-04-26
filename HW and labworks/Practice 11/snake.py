import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = 10, 0

score = 0

font = pygame.font.SysFont(None, 30)

# генерация еды с таймером
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, 10)
        y = random.randrange(0, HEIGHT, 10)
        if (x, y) not in snake:
            return {
                "pos": (x, y),
                "weight": random.choice([1,2,3]),
                "time": time.time()
            }

food = generate_food()

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: dx, dy = 0, -10
    if keys[pygame.K_DOWN]: dx, dy = 0, 10
    if keys[pygame.K_LEFT]: dx, dy = -10, 0
    if keys[pygame.K_RIGHT]: dx, dy = 10, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    # столкновение со стеной
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        break

    snake.insert(0, head)

    # съел еду
    if head == food["pos"]:
        score += food["weight"]
        food = generate_food()
    else:
        snake.pop()

    # таймер еды (5 секунд)
    if time.time() - food["time"] > 5:
        food = generate_food()

    # рисуем змею
    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s,10,10))

    # цвет еды по весу
    if food["weight"] == 1:
        color = (255,0,0)
    elif food["weight"] == 2:
        color = (0,0,255)
    else:
        color = (255,255,0)

    pygame.draw.rect(screen, color, (*food["pos"],10,10))

    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()