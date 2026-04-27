import pygame
from racer import RacerGame
from ui import Button
from persistence import load_json, save_json

pygame.init()

screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

settings = load_json("settings.json", {
    "car_color": [255,0,0]
})

leaderboard = load_json("leaderboard.json", [])

state = "menu"

play_btn = Button(120,200,150,50,"Play")
lb_btn = Button(120,270,150,50,"Leaderboard")
quit_btn = Button(120,340,150,50,"Quit")

game = None

running = True
while running:
    screen.fill((30,30,30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if play_btn.clicked(e.pos):
                    game = RacerGame(settings)
                    state = "game"

                elif lb_btn.clicked(e.pos):
                    state = "leaderboard"

                elif quit_btn.clicked(e.pos):
                    running = False

            elif state == "leaderboard":
                state = "menu"

    if state == "menu":
        play_btn.draw(screen)
        lb_btn.draw(screen)
        quit_btn.draw(screen)

    elif state == "game":
        keys = pygame.key.get_pressed()
        game.update(keys)

        if game.check_collision():
            leaderboard.append({
                "score": game.score,
                "coins": game.coin_count,
                "distance": int(game.distance)
            })

            leaderboard = sorted(
                leaderboard,
                key=lambda x: x.get("score", 0),
                reverse=True
            )[:10]

            save_json("leaderboard.json", leaderboard)
            state = "menu"

        game.draw(screen)

    elif state == "leaderboard":
        font = pygame.font.SysFont(None, 28)

        if not leaderboard:
            txt = font.render("No scores yet", True, (200,200,200))
            screen.blit(txt, (120,250))

        for i, s in enumerate(leaderboard):

            score = s.get("score", 0)
            coins = s.get("coins", 0)
            dist = s.get("distance", 0)

            txt = font.render(
                f"{i+1}. Score:{score} Coins:{coins} Dist:{dist}",
                True, (255,255,255)
            )
            screen.blit(txt, (20, 50 + i*30))

    pygame.display.update()
    clock.tick(60)

pygame.quit()