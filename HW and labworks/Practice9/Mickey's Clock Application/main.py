import pygame
from datetime import datetime
import os

pygame.init()

screen = pygame.display.set_mode((800, 600),pygame.RESIZABLE)
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()


base_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(base_path, "images", "clock.png")).convert_alpha()
background = pygame.transform.scale(background, (800, 600))

center = (400, 300)


hand = pygame.image.load(os.path.join(base_path, "images", "left_hand.png")).convert_alpha()


def scale_image(image, target_width):
    w, h = image.get_size()
    ratio = target_width / w
    return pygame.transform.scale(image, (int(w * ratio), int(h * ratio)))



hour_hand = scale_image(hand, 35)    
minute_hand = scale_image(hand, 40)  
second_hand = scale_image(hand, 45)  



def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    return rotated_image, rect


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    now = datetime.now()

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60

    hour_angle = -(hours * 30)
    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)


    rotated_hour, rect_h = rotate_hand(hour_hand, hour_angle, center)
    rotated_min, rect_m = rotate_hand(minute_hand, minute_angle, center)
    rotated_sec, rect_s = rotate_hand(second_hand, second_angle, center)


    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))


    screen.blit(rotated_hour, rect_h)
    screen.blit(rotated_min, rect_m)
    screen.blit(rotated_sec, rect_s)

    pygame.display.update()
    clock.tick(60)

pygame.quit()