import pygame as pg

pg.init()
size = width, height = 500, 500
array = []
x0, y0, x1, y1 = 0, 0, 0, 0
screen = pg.display.set_mode(size)
pg.display.flip()
running ,draw  = True, False
WHITE = (255, 255, 255)

def cancel():
    if len(array):
        del array[len(array)-1]

while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            x0, y0 = event.pos[0], event.pos[1]
            x1, y1 = 0, 0
            draw = True
        if event.type == pg.MOUSEMOTION and event.buttons[0]:
            x1 = event.pos[0] - x0
            y1 = event.pos[1] - y0
        if event.type == pg.MOUSEBUTTONUP:
            array.append((x0, y0, x1, y1))
            draw = False
        if event.type == pg.KEYDOWN and event.mod == pg.KMOD_LCTRL:
            cancel()
    if draw:
        pg.draw.rect(screen, WHITE, (x0, y0, x1, y1), 1)
    for coords in array:
        pg.draw.rect(screen, WHITE, coords, 1)
    pg.display.flip()

pg.quit()
