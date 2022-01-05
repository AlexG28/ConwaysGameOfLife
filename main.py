import pygame
from pygame import surface
from pygame.constants import WINDOWSIZECHANGED
from pygame.cursors import arrow

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

ARR = []

last = pygame.time.get_ticks()

for i in range(25):
    ARR.append([0] * 25)


def drawGridLines():
    blockSize = 20

    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

    pygame.display.update()

def drawGrid(grid):
     
    for i in range(25):
        for j in range(25):
            rect = pygame.Rect(i * 20, j * 20, 19, 19)
            if grid[i] [j] == 1:
                pygame.draw.rect(screen, [200, 200, 200], rect)
            else:
                pygame.draw.rect(screen, [0,0,0], rect)
   

    pygame.display.update()

def nextGeneration(grid):
    nextGen = []
    for i in range(25):
        nextGen.append([0] * 25)
    
    def countNeighbours(i, j):
        counter = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                if grid[i + x] [j + y] == 1:
                    counter += 1

        if grid[i] [j] == 1:
            counter -= 1

        return counter 
    
    for i in range(1,24):
        for j in range(1,24):           
            
            nOfNeighbour = countNeighbours(i, j)
            
            if grid[i][j] == 1 and (nOfNeighbour == 3 or nOfNeighbour == 2):
                nextGen[i][j] = 1
            elif  grid[i][j] == 0 and nOfNeighbour == 3:
                nextGen[i][j] = 1
            else:
                if grid[i][j] == 1:
                    nextGen[i][j] = 0                


    return nextGen



if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode([WINDOW_HEIGHT, WINDOW_WIDTH])
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    pygame.display.update()

    running = True
    gameOfLife = False

    while running:
        drawGridLines()
        
        if gameOfLife:
            
            now = pygame.time.get_ticks()
            
            if now - last >= 500:
                ARR = nextGeneration(ARR)
                drawGrid(ARR)
                last = now


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()

                if mouse_press[0]:                    
                    position = pygame.mouse.get_pos()

                    x = int(position[0] / 20)
                    y = int(position[1] / 20)

                    #print(f"x: {x}        y: {y}")

                    ARR[x][y] = 1

                    rect = pygame.Rect(x * 20, y * 20, 19, 19)
                    pygame.draw.rect(screen, [200, 200, 200], rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                   
                    print("start algorithm")
                    gameOfLife = True

                if event.key == pygame.K_BACKSPACE:
                    print("backspace, end game")
                    gameOfLife = False


    pygame.quit()