import pygame
from player import MusicPlayer
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

player = MusicPlayer()

running = True
bar_values = [50] * 20
last_update = 0

def draw_soundbars(screen, x, y, width, height, bar_values):
    bars = len(bar_values)
    bar_width = width // bars

    for i in range(bars):
        h = bar_values[i]
        rect = pygame.Rect(x + i * bar_width, y + (height - h), bar_width - 3, h)
        pygame.draw.rect(screen, (0, 200, 0), rect)


while running:
    screen.fill((255, 255, 255))
    
    current_time = pygame.time.get_ticks()

    if current_time - last_update > 200:
        bar_values = [random.randint(20, 100) for _ in range(20)]
        last_update = current_time

    draw_soundbars(screen, 50, 250, 500, 100, bar_values)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.previous()
            elif event.key == pygame.K_q:
                running = False
    

    text = font.render(f"Track: {player.get_current_track()}", True, (0, 0, 0))
    screen.blit(text, (200,200))

    pygame.display.update()

pygame.quit()