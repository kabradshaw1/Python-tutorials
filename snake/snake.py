from operator import truediv
from turtle import width


class cube(object):
    row = 0
    W = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=false):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w, y))

def redrawWindow(surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass

def randomSnack(row, items):
    pass

def message_box(subect, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((225, 0, 0), (10, 10))
    flag = true

    clock = pygame.time.clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

    pass