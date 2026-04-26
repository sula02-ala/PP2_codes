import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)


def reset_game():
    """Сброс игры"""
    player = pygame.Rect(180, 500, 40, 60)
    enemy = pygame.Rect(random.randint(0, 360), -100, 40, 60)
    coins = []
    coin_score = 0
    enemy_speed = 5
    game_over = False
    return player, enemy, coins, coin_score, enemy_speed, game_over


def spawn_coin(coins):
    """Создание монеты с весом"""
    x = random.randint(20, WIDTH - 20)
    weight = random.choice([1, 2, 3])  # вес монеты
    coins.append({
        "rect": pygame.Rect(x, -50, 20, 20),
        "weight": weight
    })


player, enemy, coins, coin_score, enemy_speed, game_over = reset_game()
coin_timer = 0

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, enemy, coins, coin_score, enemy_speed, game_over = reset_game()


    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.x < WIDTH - 40:
            player.x += 5


        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(0, 360)

        enemy_speed = 5 + coin_score // 5

        coin_timer += 1
        if coin_timer > 50:
            spawn_coin(coins)
            coin_timer = 0

        for coin in coins[:]:
            coin["rect"].y += enemy_speed


            if player.colliderect(coin["rect"]):
                coin_score += coin["weight"]
                coins.remove(coin)

            elif coin["rect"].y > HEIGHT:
                coins.remove(coin)


        if player.colliderect(enemy):
            game_over = True


    pygame.draw.rect(screen, (0, 255, 0), player)


    pygame.draw.rect(screen, (255, 0, 0), enemy)


    for coin in coins:
        if coin["weight"] == 1:
            color = (255, 215, 0)   # золотая
        elif coin["weight"] == 2:
            color = (0, 255, 255)   # голубая
        else:
            color = (255, 0, 255)   # фиолетовая

        pygame.draw.circle(screen, color, coin["rect"].center, 10)


    score_text = font.render(f"Coins: {coin_score}", True, (255, 255, 255))
    screen.blit(score_text, (220, 10))


    hint_text = font.render("Press R to restart", True, (200, 200, 200))
    screen.blit(hint_text, (80, 560))


    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (120, 280))

    pygame.display.update()
    clock.tick(60)

pygame.quit()