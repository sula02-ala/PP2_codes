import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Canvas (ВАЖНО!)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

color = (0, 0, 0)
mode = "draw"

drawing = False
start_pos = (0, 0)

font = pygame.font.SysFont(None, 24)

running = True
while running:

    # Рисуем canvas (он сохраняет всё)
    screen.blit(canvas, (0, 0))

    # Текст управления
    controls = [
        "1 - Draw",
        "2 - Rectangle",
        "3 - Circle",
        "4 - Eraser",
        "R/G/B - Change color"
    ]

    for i, text in enumerate(controls):
        render = font.render(text, True, (0, 0, 0))
        screen.blit(render, (10, 10 + i * 20))

    mode_text = font.render(f"Mode: {mode}", True, (0, 0, 0))
    screen.blit(mode_text, (650, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (
                    end_pos[0] - start_pos[0],
                    end_pos[1] - start_pos[1]
                ))
                pygame.draw.rect(canvas, color, rect, 2)

            if mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(canvas, color, start_pos, radius, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(canvas, color, event.pos, 5)

            if mode == "erase":
                pygame.draw.circle(canvas, (255, 255, 255), event.pos, 10)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "draw"
            if event.key == pygame.K_2:
                mode = "rect"
            if event.key == pygame.K_3:
                mode = "circle"
            if event.key == pygame.K_4:
                mode = "erase"

            if event.key == pygame.K_r:
                color = (255, 0, 0)
            if event.key == pygame.K_g:
                color = (0, 255, 0)
            if event.key == pygame.K_b:
                color = (0, 0, 255)

    pygame.display.update()
    clock.tick(60)

pygame.quit()