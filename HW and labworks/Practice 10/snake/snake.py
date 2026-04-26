import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = 10, 0

score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

def generate_food():
    while True:
        x = random.randrange(0, WIDTH, 10)
        y = random.randrange(0, HEIGHT, 10)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx, dy = 0, -10
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 10
    if keys[pygame.K_LEFT]:
        dx, dy = -10, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 10, 0

    # Move snake
    head = (snake[0][0] + dx, snake[0][1] + dy)

    # Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("GAME OVER")
        break

    snake.insert(0, head)

    # Eating food
    if head == food:
        score += 1
        food = generate_food()
    else:
        snake.pop()

    # Level system
    if score >= 5:
        level = 2
    if score >= 10:
        level = 3

    speed = 10 + level * 3

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))

    # Score display
    text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()