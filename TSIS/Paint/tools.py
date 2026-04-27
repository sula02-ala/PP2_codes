import pygame
import math


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if px < 0 or px >= surface.get_width() or py < 0 or py >= surface.get_height():
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        stack.append((px+1, py))
        stack.append((px-1, py))
        stack.append((px, py+1))
        stack.append((px, py-1))



def line(s, c, a, b, size):
    pygame.draw.line(s, c, a, b, size)

def rect(s, c, a, b, size):
    pygame.draw.rect(s, c, pygame.Rect(a, (b[0]-a[0], b[1]-a[1])), size)

def circle(s, c, a, b, size):
    r = int(((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5)
    pygame.draw.circle(s, c, a, r, size)

def square(s, c, a, b, size):
    side = abs(b[0]-a[0])
    pygame.draw.rect(s, c, (*a, side, side), size)

def ellipse(s, c, a, b, size):
    pygame.draw.ellipse(s, c, pygame.Rect(a, (b[0]-a[0], b[1]-a[1])), size)



def right_triangle(s, c, a, b, size):
    pts = [a, (b[0], a[1]), b]
    pygame.draw.polygon(s, c, pts, size)

def equilateral_triangle(s, c, a, b, size):
    side = abs(b[0]-a[0])
    h = side * math.sqrt(3)/2
    pts = [a, (a[0]+side, a[1]), (a[0]+side/2, a[1]-h)]
    pygame.draw.polygon(s, c, pts, size)

def isosceles_triangle(s, c, a, b, size):
    pts = [a, b, (2*a[0]-b[0], b[1])]
    pygame.draw.polygon(s, c, pts, size)



def rhombus(s, c, a, b, size):
    cx, cy = a
    dx, dy = abs(b[0]-a[0]), abs(b[1]-a[1])
    pts = [(cx,cy-dy),(cx+dx,cy),(cx,cy+dy),(cx-dx,cy)]
    pygame.draw.polygon(s, c, pts, size)

def pentagon(s, c, a, b, size):
    cx, cy = a
    r = abs(b[0]-a[0])
    pts = [(cx + r*math.cos(i*2*math.pi/5), cy + r*math.sin(i*2*math.pi/5)) for i in range(5)]
    pygame.draw.polygon(s, c, pts, size)

def hexagon(s, c, a, b, size):
    cx, cy = a
    r = abs(b[0]-a[0])
    pts = [(cx + r*math.cos(i*2*math.pi/6), cy + r*math.sin(i*2*math.pi/6)) for i in range(6)]
    pygame.draw.polygon(s, c, pts, size)

def star(s, c, a, b, size):
    cx, cy = a
    r = abs(b[0]-a[0])
    pts = []
    for i in range(10):
        ang = i * math.pi/5
        rr = r if i%2==0 else r/2
        pts.append((cx + rr*math.cos(ang), cy + rr*math.sin(ang)))
    pygame.draw.polygon(s, c, pts, size)