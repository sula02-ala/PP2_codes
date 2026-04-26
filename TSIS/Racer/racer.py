import pygame
import random

WIDTH, HEIGHT = 400, 600
LANES = [60, 150, 240, 330]

class RacerGame:
    def __init__(self, settings):
        self.player = pygame.Rect(180, 500, 40, 60)

        self.enemies = []
        self.coins = []

        self.speed = 5
        self.score = 0
        self.distance = 0
        self.coin_count = 0

        self.settings = settings

        self.font = pygame.font.SysFont(None, 26)
        self.road_offset = 0

    def spawn_enemy(self):
        lane = random.choice(LANES)
        if abs(lane - self.player.x) > 80:
            self.enemies.append(pygame.Rect(lane, -100, 40, 60))

    def spawn_coin(self):
        lane = random.choice(LANES)
        self.coins.append(pygame.Rect(lane+10, -50, 20, 20))

    def update(self, keys):

        if keys[pygame.K_UP]:
            self.speed += 0.2
        if keys[pygame.K_DOWN]:
            self.speed -= 0.2

        self.speed = max(3, min(self.speed, 12))


        self.distance += self.speed
        self.score += int(self.speed)


        if random.randint(0,100) < 3:
            self.spawn_enemy()
        if random.randint(0,100) < 5:
            self.spawn_coin()


        for e in self.enemies:
            e.y += self.speed
        for c in self.coins:
            c.y += self.speed


        self.enemies = [e for e in self.enemies if e.y < HEIGHT]
        self.coins = [c for c in self.coins if c.y < HEIGHT]


        for c in self.coins[:]:
            if self.player.colliderect(c):
                self.coin_count += 1
                self.coins.remove(c)


        self.road_offset += self.speed
        if self.road_offset > 40:
            self.road_offset = 0

    def check_collision(self):
        for e in self.enemies:
            if self.player.colliderect(e):
                return True
        return False

    def draw_road(self, screen):
        screen.fill((30,30,30))

        pygame.draw.rect(screen, (50,50,50), (0,0,WIDTH,HEIGHT))

        for y in range(-40, HEIGHT, 40):
            pygame.draw.rect(screen, (255,255,255), (95, y+self.road_offset, 5, 20))
            pygame.draw.rect(screen, (255,255,255), (195, y+self.road_offset, 5, 20))
            pygame.draw.rect(screen, (255,255,255), (295, y+self.road_offset, 5, 20))

    def draw(self, screen):
        self.draw_road(screen)

        pygame.draw.rect(screen, self.settings["car_color"], self.player)

        for e in self.enemies:
            pygame.draw.rect(screen, (255,0,0), e)

        for c in self.coins:
            pygame.draw.circle(screen, (255,215,0), c.center, 10)

        screen.blit(self.font.render(f"Score: {self.score}", True, (255,255,255)), (10,10))
        screen.blit(self.font.render(f"Coins: {self.coin_count}", True, (255,255,255)), (10,30))
        screen.blit(self.font.render(f"Speed: {round(self.speed,1)}", True, (255,255,255)), (10,50))
        screen.blit(self.font.render(f"Dist: {int(self.distance)}", True, (255,255,255)), (10,70))