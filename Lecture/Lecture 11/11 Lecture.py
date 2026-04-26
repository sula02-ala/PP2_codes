import pygame
import os
import random

pygame.init()
SPAWN_COIN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN_EVENT, 2000)  # каждые 2 секунды

def spawn_coin():
    return pygame.Rect(
        random.randint(20, W - 20),
        random.randint(50, ground_y - 20),
        12, 12
    )


# --- настройки ---
W, H = 800, 500
FLAGS = pygame.RESIZABLE
sc = pygame.display.set_mode((W, H), FLAGS)
pygame.display.set_caption("Platformer Pro")
clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (20,20,20)

font = pygame.font.SysFont("arial", 18)

# --- пути ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "image")

def load_image(name, size=None):
    path = os.path.join(IMG_DIR, name)
    if not os.path.exists(path):
        print("❌ Не найден:", path)
        surf = pygame.Surface((20,20))
        surf.fill((0,0,255))
        return surf
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img

hero_img = load_image("hero.png", (20,30))
coin_img = load_image("coin.png", (36,36))

# --- игрок ---
PLAYER_W, PLAYER_H = 20, 30
x, y = 100, 100
vx, vy = 0, 0
speed = 5
GRAVITY = 1
JUMP = -15

hero_rect = pygame.Rect(x, y, PLAYER_W, PLAYER_H)

on_ground = False
jumps_left = 2

# --- земля ---
ground_y = H - 40

# --- платформы ---
blocks = []  # (rect, spawn_time)

# --- монеты ---
coins = []
for _ in range(6):
    coins.append(pygame.Rect(random.randint(50, 750), random.randint(50, 400), 12, 12))

# --- счёт ---
score = 0
start_time = pygame.time.get_ticks()

# --- мышь ---
drawing = False
start_pos = None

running = True
while running:

    dt = clock.tick(60)
    sc.fill(WHITE)

    # --- события ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == SPAWN_COIN_EVENT:
            if len(coins) < 10:  # лимит
                coins.append(spawn_coin())


        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            sc = pygame.display.set_mode((W, H), FLAGS)
            ground_y = H - 40

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end = pygame.mouse.get_pos()
            rect = pygame.Rect(start_pos, (end[0]-start_pos[0], end[1]-start_pos[1]))
            rect.normalize()

            if rect.w > 10 and rect.h > 10:
                blocks.append((rect, pygame.time.get_ticks()))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jumps_left > 0:
                    vy = JUMP
                    jumps_left -= 1
                    on_ground = False

    # --- управление ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vx = -speed
    elif keys[pygame.K_RIGHT]:
        vx = speed
    else:
        vx = 0

    x += vx

    # --- гравитация ---
    vy += GRAVITY
    y += vy

    hero_rect.topleft = (x, y)

    on_ground = False

    # --- столкновения с платформами ---
    new_blocks = []
    current_time = pygame.time.get_ticks()

    for rect, spawn_time in blocks:

        # удаление через 60 сек
        if current_time - spawn_time > 60000:
            continue
        else:
            new_blocks.append((rect, spawn_time))

        if hero_rect.colliderect(rect):

            # сверху
            if vy > 0 and hero_rect.bottom <= rect.top + 10:
                hero_rect.bottom = rect.top
                y = hero_rect.y
                vy = 0
                on_ground = True
                jumps_left = 2

            # снизу
            elif vy < 0 and hero_rect.top >= rect.bottom - 10:
                hero_rect.top = rect.bottom
                y = hero_rect.y
                vy = 0

    blocks = new_blocks

    # --- земля ---
    if hero_rect.bottom >= ground_y:
        hero_rect.bottom = ground_y
        y = hero_rect.y
        vy = 0
        on_ground = True
        jumps_left = 2

    # --- монеты ---
    for c in coins[:]:
        if hero_rect.colliderect(c):
            coins.remove(c)
            score += 1

    # --- таймер ---
    elapsed_sec = (pygame.time.get_ticks() - start_time) // 1000

    # --- рисование ---
    pygame.draw.line(sc, GREEN, (0, ground_y), (W, ground_y), 3)

    for rect, _ in blocks:
        pygame.draw.rect(sc, RED, rect, 2)

    for c in coins:
        sc.blit(coin_img, (c.x, c.y))

    sc.blit(hero_img, (hero_rect.x, hero_rect.y))

    # HUD
    hud = font.render(f"Score: {score} | Time: {elapsed_sec}s | Jumps: {jumps_left}", True, BLACK)
    sc.blit(hud, (10, 10))

    pygame.display.update()

pygame.quit()