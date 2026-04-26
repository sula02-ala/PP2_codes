import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()


player = pygame.Rect(180, 500, 40, 60)

enemy = pygame.Rect(random.randint(0, 360), -100, 40, 60)

coins = []

coin_count = 0
speed = 5

font = pygame.font.SysFont(None, 36)

def spawn_coin():
    x = random.randint(20, WIDTH-20)
    coins.append(pygame.Rect(x, -50, 20, 20))

running = True
coin_timer = 0

while running:
    screen.fill((30, 30, 30))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH-40:
        player.x += 5

    enemy.y += speed
    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(0, 360)

# Coin spawn
    coin_timer += 1
    if coin_timer > 60:
        spawn_coin()
        coin_timer = 0

# Coins movement
    for coin in coins[:]:
        coin.y += speed

        # Collision with player
        if player.colliderect(coin):
            coins.remove(coin)
            coin_count += 1

        elif coin.y > HEIGHT:
            coins.remove(coin)

# Draw player, enemy, coins
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    for coin in coins:
        pygame.draw.circle(screen, (255, 215, 0), coin.center, 10)

# Collision with enemy
    if player.colliderect(enemy):
        print("GAME OVER")
        running = False

# Display coins
    text = font.render(f"Coins: {coin_count}", True, (255,255,255))
    screen.blit(text, (WIDTH - 150, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()