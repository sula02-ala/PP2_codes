import pygame
import random
import os

GRID = 10
W, H = 600, 400

class SnakeGame:
    def __init__(self, settings):
        self.snake = [(100,100)]
        self.dx, self.dy = GRID, 0

        self.settings = settings
        self.score = 0
        self.level = 1

        self.base_speed = settings.get("speed", 10)
        self.speed = self.base_speed

        self.power = None
        self.power_timer = 0
        self.powerup = None

        self.obstacles = []

        base = os.path.dirname(__file__)

        pygame.mixer.init()
        try:
            self.move_sound = pygame.mixer.Sound(os.path.join(base, "assets", "pong.wav"))
        except:
            self.move_sound = None

        def load(name):
            path = os.path.join(base, "assets", name)
            img = pygame.image.load(path)
            return pygame.transform.scale(img, (20,20))

        self.food_data = {
            "apple": (load("apple.png"), 1),
            "lemon": (load("lemon.png"), 2),
            "orange": (load("orange.png"), 3),
            "watermelon": (load("watermelon.png"), 10)
        }

        self.food = self.spawn_food()

    def spawn_food(self):
        while True:
            t = random.choice(list(self.food_data.keys()))
            pos = (random.randrange(0,W,GRID), random.randrange(0,H,GRID))
            if pos not in self.snake and pos not in self.obstacles:
                return {"type":t,"pos":pos}

    def spawn_powerup(self):
        while True:
            pos = (random.randrange(0,W,GRID), random.randrange(0,H,GRID))
            if pos not in self.snake and pos not in self.obstacles:
                break

        self.powerup = {
            "type": random.choice(["speed","slow","shield"]),
            "pos": pos,
            "time": pygame.time.get_ticks()
        }

    def spawn_obstacles(self):
        self.obstacles = []
        for _ in range(10):
            while True:
                pos = (random.randrange(0,W,GRID), random.randrange(0,H,GRID))
                if pos not in self.snake:
                    self.obstacles.append(pos)
                    break

    def update(self):
        nx = self.snake[0][0] + self.dx
        ny = self.snake[0][1] + self.dy

#если щит — проходим через края
        if self.power == "shield":
            nx %= W
            ny %= H

        head = (nx, ny)

        if self.settings.get("sound", True) and self.move_sound:
            self.move_sound.play()


        if self.power != "shield":
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                return False


        if head in self.snake:
            if self.power == "shield":
                self.power = None
            else:
                return False

#препятствия
        if head in self.obstacles:
            if self.power != "shield":
                return False

        self.snake.insert(0, head)

#еда
        fx, fy = self.food["pos"]
        if abs(head[0]-fx)<15 and abs(head[1]-fy)<15:
            _, pts = self.food_data[self.food["type"]]
            self.score += pts

            for _ in range(pts):
                self.snake.append(self.snake[-1])

            self.food = self.spawn_food()

            if random.randint(0,100) < 40:
                self.spawn_powerup()
        else:
            self.snake.pop()

#буст
        if self.powerup:
            px, py = self.powerup["pos"]
            if abs(head[0]-px)<10 and abs(head[1]-py)<10:
                self.power = self.powerup["type"]
                self.power_timer = pygame.time.get_ticks()
                self.powerup = None


        if self.power and pygame.time.get_ticks() - self.power_timer > 5000:
            self.power = None

        self.speed = self.base_speed
        if self.power == "speed":
            self.speed += 5
        elif self.power == "slow":
            self.speed -= 3

#уровень
        if self.score >= self.level * 10:
            self.level += 1
            self.base_speed += 1
            if self.level >= 3:
                self.spawn_obstacles()

        return True

    def draw(self, screen):
        if self.settings.get("grid", True):
            for x in range(0,W,GRID):
                pygame.draw.line(screen,(50,50,50),(x,0),(x,H))
            for y in range(0,H,GRID):
                pygame.draw.line(screen,(50,50,50),(0,y),(W,y))

        for s in self.snake:
            pygame.draw.rect(screen,self.settings.get("snake_color",(0,255,0)),(*s,GRID,GRID))

        img,_ = self.food_data[self.food["type"]]
        screen.blit(img,self.food["pos"])

        for o in self.obstacles:
            pygame.draw.rect(screen,(120,120,120),(*o,GRID,GRID))

        if self.powerup:
            color = (0,255,0) if self.powerup["type"]=="speed" else (0,0,255)
            pygame.draw.rect(screen,color,(*self.powerup["pos"],10,10))