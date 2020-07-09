import pygame as pg
pg.init()

size = width, height = 300, 300
work, domove  = True, False
x,y,x_last,y_last = 0,0,0,0
BLACK = pg.Color(0, 0, 0)

def draw(x,y):
    screen.fill(BLACK)
    pg.draw.rect(screen, pg.color.Color('red'), (x,y,70,70))
    return x,y

def check():
    x,y = event.pos
    r1,r2 = x - x_last,y - y_last
    if abs(r1)> 70 or abs(r2)> 70:
        print(f"расстояние {r1,r2}")
        print(f"текущие координаты {x,y}")
        print(f"последнеее положение {x_last,y_last}")
        return False
    return True

screen = pg.display.set_mode(size)
draw(0,0)
pg.display.flip()

while work:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            work = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            work = False
        if event.type == pg.MOUSEBUTTONDOWN:
            status = check()
            if status:
                domove = True
        if event.type == pg.MOUSEMOTION and domove:
            x, y = event.pos
            x_last,y_last = draw(x,y)
        if event.type == pg.MOUSEBUTTONUP: 
            domove = False
    pg.display.flip()

pg.quit()