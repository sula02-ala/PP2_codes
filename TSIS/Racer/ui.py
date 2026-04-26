import pygame

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont(None, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, (200,200,200), self.rect)
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)
        txt = self.font.render(self.text, True, (0,0,0))
        screen.blit(txt, (self.rect.x+10, self.rect.y+10))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)