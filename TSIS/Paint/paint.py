import pygame, sys, os
from datetime import datetime
import tools

pygame.init()

W, H = 1000, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("TSIS2 Paint PRO")

canvas = pygame.Surface((W, H-100))
canvas.fill((255,255,255))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

color = (0,0,0)
brush = 3
mode = "pencil"

drawing = False
start = None
last = None


typing = False
text_input = ""
text_pos = (0,0)


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


class Button:
    def __init__(self, x,y,w,h,text,mode_name):
        self.rect = pygame.Rect(x,y,w,h)
        self.text=text
        self.mode=mode_name

    def draw(self):
        pygame.draw.rect(screen,(200,200,200),self.rect)
        pygame.draw.rect(screen,(0,0,0),self.rect,1)
        screen.blit(font.render(self.text,True,(0,0,0)),(self.rect.x+5,self.rect.y+5))

    def click(self,pos):
        return self.rect.collidepoint(pos)

buttons = [
    Button(10,10,70,30,"Pencil","pencil"),
    Button(90,10,60,30,"Line","line"),
    Button(160,10,60,30,"Rect","rect"),
    Button(230,10,60,30,"Circle","circle"),
    Button(300,10,70,30,"Square","square"),
    Button(380,10,70,30,"Ellipse","ellipse"),
    Button(460,10,70,30,"R-Tri","rt"),
    Button(540,10,70,30,"Eq-Tri","eq"),
    Button(620,10,70,30,"Iso-Tri","iso"),
    Button(700,10,70,30,"Rhomb","rhomb"),
    Button(780,10,70,30,"Star","star"),
    Button(860,10,70,30,"Hex","hex"),
    Button(940,10,50,30,"Text","text"),
]

# кнопки толщины кисти
brush_buttons = [
    Button(10,50,80,25,"Thin","thin"),
    Button(100,50,80,25,"Medium","medium"),
    Button(190,50,80,25,"Thick","thick"),
]


colors = [
    (0,0,0),(255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(255,0,255),(0,255,255),
    (255,165,0),(128,0,128),(0,128,128)
]

# создаем прямоугольники для выбора цвета
color_rects = []
for i,c in enumerate(colors):
    rect = pygame.Rect(300+i*30,50,25,25)
    color_rects.append((rect,c))

clear_btn = pygame.Rect(880,50,100,25)

running = True
while running:
    screen.fill((220,220,220))
    screen.blit(canvas,(0,100))


    for b in buttons:
        b.draw()

    for b in brush_buttons:
        b.draw()


    for rect,c in color_rects:
        pygame.draw.rect(screen,c,rect)
        pygame.draw.rect(screen,(0,0,0),rect,1)

    pygame.draw.rect(screen,(255,100,100),clear_btn)
    screen.blit(font.render("CLEAR",True,(0,0,0)),(890,55))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("screenshots/img_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)


            if typing:
                if e.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    canvas.blit(img, text_pos)
                    typing = False
                    text_input = ""
                elif e.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""
                elif e.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += e.unicode

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = e.pos


            for b in buttons:
                if b.click(pos):
                    mode = b.mode
                    drawing = False
                    start = None


            for b in brush_buttons:
                if b.click(pos):
                    if b.mode=="thin": brush=2
                    if b.mode=="medium": brush=5
                    if b.mode=="thick": brush=10


            for rect,c in color_rects:
                if rect.collidepoint(pos):
                    color = c


            if clear_btn.collidepoint(pos):
                canvas.fill((255,255,255))
                drawing=False
                start=None


            if pos[1] > 100:
                if mode == "text":
                    typing = True
                    text_pos = (pos[0], pos[1]-100)
                    text_input = ""
                else:
                    drawing = True
                    start = (pos[0], pos[1]-100)
                    last = start

        if e.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end = (e.pos[0], e.pos[1]-100)

                mapping = {
                    "line":"line","rect":"rect","circle":"circle","square":"square",
                    "ellipse":"ellipse","rt":"right_triangle","eq":"equilateral_triangle",
                    "iso":"isosceles_triangle","rhomb":"rhombus","star":"star","hex":"hexagon"
                }

                if mode in mapping:
                    getattr(tools, mapping[mode])(canvas, color, start, end, brush)

            drawing = False

        if e.type == pygame.MOUSEMOTION and drawing:
            pos = (e.pos[0], e.pos[1]-100)
            if mode == "pencil":
                tools.line(canvas,color,last,pos,brush)
                last = pos

# предпросмотр фигуры
    if drawing and start and mode not in ["pencil","text"]:
        temp = canvas.copy()
        pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]-100)

        mapping = {
            "line":"line","rect":"rect","circle":"circle","square":"square",
            "ellipse":"ellipse","rt":"right_triangle","eq":"equilateral_triangle",
            "iso":"isosceles_triangle","rhomb":"rhombus","star":"star","hex":"hexagon"
        }

        if mode in mapping:
            getattr(tools, mapping[mode])(temp, color, start, pos, brush)

        screen.blit(temp,(0,100))


    if typing:
        preview = font.render(text_input, True, color)
        screen.blit(preview, (text_pos[0], text_pos[1]+100))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()