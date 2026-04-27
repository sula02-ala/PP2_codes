import pygame
import random
import os
import json
from game import SnakeGame
from db import init_db, save_score_db, get_top_scores_db

pygame.init()
pygame.mixer.init()
init_db()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

SETTINGS_FILE = "settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    return {
        "snake_color": data.get("snake_color", [0,255,0]),
        "grid": data.get("grid", True),
        "speed": data.get("speed", 10),
        "sound": data.get("sound", True)
    }

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)

settings = load_settings()

base = os.path.dirname(__file__)
try:
    pygame.mixer.music.load(os.path.join(base, "assets", "gamesound.mp3"))
    pygame.mixer.music.play(-1)
except:
    pass

def apply_sound():
    pygame.mixer.music.set_volume(1 if settings["sound"] else 0)

apply_sound()

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, (200,200,200), self.rect)
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)
        txt = font.render(self.text, True, (0,0,0))
        screen.blit(txt, (self.rect.x+10, self.rect.y+10))

    def click(self, pos):
        return self.rect.collidepoint(pos)

play = Button(200,70,200,50,"Play")
lb = Button(200,130,200,50,"Leaderboard")
setb = Button(200,190,200,50,"Settings")
quitb = Button(200,250,200,50,"Quit")
back = Button(10,10,100,40,"Back")

state = "menu"
game = None

running = True
while running:
    screen.fill((30,30,30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_m:
                settings["sound"] = not settings["sound"]
                apply_sound()
                save_settings(settings)

        if state == "menu":
            if e.type == pygame.MOUSEBUTTONDOWN:
                if play.click(e.pos):
                    game = SnakeGame(settings)
                    state = "game"
                elif lb.click(e.pos):
                    state = "leaderboard"
                elif setb.click(e.pos):
                    state = "settings"
                elif quitb.click(e.pos):
                    running = False

        elif state == "game":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP: game.dx, game.dy = 0,-10
                elif e.key == pygame.K_DOWN: game.dx, game.dy = 0,10
                elif e.key == pygame.K_LEFT: game.dx, game.dy = -10,0
                elif e.key == pygame.K_RIGHT: game.dx, game.dy = 10,0

        elif state == "leaderboard":
            if e.type == pygame.MOUSEBUTTONDOWN:
                if back.click(e.pos):
                    state = "menu"

        elif state == "settings":
            if e.type == pygame.MOUSEBUTTONDOWN:
                if back.click(e.pos):
                    state = "menu"

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_g:
                    settings["grid"] = not settings["grid"]
                elif e.key == pygame.K_c:
                    settings["snake_color"] = [random.randint(0,255) for _ in range(3)]
                elif e.key == pygame.K_UP:
                    settings["speed"] += 1
                elif e.key == pygame.K_DOWN:
                    settings["speed"] = max(1, settings["speed"] - 1)

                save_settings(settings)

    if state == "menu":
        play.draw()
        lb.draw()
        setb.draw()
        quitb.draw()

    elif state == "game":
        alive = game.update()

        if not alive:
            ok = save_score_db("player", game.score, game.level)
            print("Saved:", ok)
            state = "menu"

        game.draw(screen)

        screen.blit(font.render(f"Score: {game.score}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Level: {game.level}", True, (255,255,255)), (10,30))
#бусты
        if hasattr(game, "power") and game.power:
            remaining = max(0, 5 - (pygame.time.get_ticks() - game.power_timer)//1000)
            screen.blit(font.render(f"Power: {game.power} ({remaining}s)", True, (0,255,255)), (10,60))

    elif state == "leaderboard":
        back.draw()
        data = get_top_scores_db()

        if not data:
            screen.blit(font.render("No scores yet", True, (200,200,200)), (200,150))

        for i, (name, score) in enumerate(data):
            txt = font.render(f"{i+1}. {name} - {score}", True, (255,255,255))
            screen.blit(txt, (150, 80 + i * 30))

    elif state == "settings":
        back.draw()
        screen.blit(font.render("SETTINGS", True, (255,255,255)), (230,40))
        screen.blit(font.render(f"G - Grid: {settings['grid']}", True, (255,255,255)), (150,100))
        screen.blit(font.render("C - Change Color", True, (255,255,255)), (150,130))
        screen.blit(font.render("UP/DOWN - Speed", True, (255,255,255)), (150,160))
        screen.blit(font.render("M - Sound ON/OFF", True, (255,255,255)), (150,190))
        screen.blit(font.render(f"Speed: {settings['speed']}", True, (255,255,255)), (150,220))

        pygame.draw.rect(screen, settings["snake_color"], (420,130,60,60))

    if state == "game" and game:
        clock.tick(game.speed)
    else:
        clock.tick(60)

    pygame.display.update()

pygame.quit()