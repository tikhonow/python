import pygame as pg
import math

pg.init()
size = width, height = 500, 500
rad = 200
screen = pg.display.set_mode(size)
points = []

for i in range(1,361):
    x = int(math.cos(math.radians(i)) * rad) + height//2
    y = int(math.sin(math.radians(i)) * rad) + height//2
    points.append((x,y))

mult = 2
pause = True
work = True
color = pg.Color('white')
hcolor = color.hsva

while work:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            work = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and pause:
            pause = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE and not pause:
            pause = True
    if pause:
        hcolor = ((hcolor[0] + 0.1) % 256,  hcolor[1],  hcolor[2],  hcolor[3])
        screen.fill((0, 0, 0))
        for i in range(360):
            pg.draw.aaline(screen, hcolor, points[i], points[(round(i * mult)) % 360])
        pg.draw.circle(screen, hcolor, (width // 2, height // 2), rad, 1)
        pg.display.flip()
        mult += 0.01
        
pg.quit()