import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255,255,255))

color = (0,0,0)
mode = "draw"

start = (0,0)
drawing = False

font = pygame.font.SysFont(None, 24)

clock = pygame.time.Clock()

running = True
while running:
    screen.blit(canvas, (0,0))

    # UI текст
    texts = [
        "1 Draw",
        "2 Square",
        "3 Right Triangle",
        "4 Equilateral Triangle",
        "5 Rhombus",
        "E Eraser"
    ]

    for i,t in enumerate(texts):
        screen.blit(font.render(t, True, (0,0,0)), (10,10+i*20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: mode="draw"
            if event.key == pygame.K_2: mode="square"
            if event.key == pygame.K_3: mode="rt"
            if event.key == pygame.K_4: mode="eq"
            if event.key == pygame.K_5: mode="rhombus"
            if event.key == pygame.K_e: mode="erase"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing=True
            start = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing=False
            end = event.pos

            if mode == "square":
                size = abs(end[0]-start[0])
                pygame.draw.rect(canvas, color, (*start, size, size), 2)

            if mode == "rt":
                points = [start, (end[0], start[1]), end]
                pygame.draw.polygon(canvas, color, points, 2)

            if mode == "eq":
                side = abs(end[0]-start[0])
                h = side * math.sqrt(3)/2
                points = [
                    start,
                    (start[0]+side, start[1]),
                    (start[0]+side/2, start[1]-h)
                ]
                pygame.draw.polygon(canvas, color, points, 2)

            if mode == "rhombus":
                cx, cy = start
                dx = abs(end[0]-start[0])
                dy = abs(end[1]-start[1])
                points = [
                    (cx, cy-dy),
                    (cx+dx, cy),
                    (cx, cy+dy),
                    (cx-dx, cy)
                ]
                pygame.draw.polygon(canvas, color, points, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(canvas, color, event.pos, 5)
            if mode == "erase":
                pygame.draw.circle(canvas, (255,255,255), event.pos, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()