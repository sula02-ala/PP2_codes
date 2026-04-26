import pygame
pygame.init()

screen = pygame.display.set_mode((600,400),pygame.RESIZABLE)
pygame.display.set_caption("Hello") #название окна


clock=pygame.time.Clock()
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)

screen.fill(white)
pygame.draw.rect(screen, green , (0, 350, 600 ,50))
pygame.draw.circle(screen,green,(500,80),10)

pygame.display.update()


#keyboard
x=300
y=200
speed=5

#mouse
drawing=False
start_pos=None



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing= True
            start_pos= event.pos #orig
            print(start_pos)

        elif event.type == pygame.MOUSEMOTION and drawing:
            pos = event.pos 
            width = pos[0] - start_pos[0]
            height = pos [1]- start_pos[1]
            pygame.draw.rect(screen,green,pygame.Rect(start_pos[0],start_pos[1],width,height))
    #hero
    hero=pygame.Surface((40,50))
    hero.fill(red)

    rect=hero.get_rect(center=(300,200))
    screen.blit(hero,rect)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    pygame.draw.rect(screen,green,(x,y,20,20))

    #jumping hero

    pround = 330

    clock.tick(60)
    pygame.display.flip()