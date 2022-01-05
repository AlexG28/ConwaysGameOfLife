import pygame
from pygame import surface
from pygame.constants import WINDOWSIZECHANGED

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

ARR = [[0] * 25] * 25


def drawGrid():
    blockSize = 20

    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

    pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode([WINDOW_HEIGHT, WINDOW_WIDTH])
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    pygame.display.update()

    running = True
    gameOfLife = False

    while running:
        drawGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()

                if mouse_press[0]:                    
                    position = pygame.mouse.get_pos()

                    x = int(position[0] / 20)
                    y = int(position[1] / 20)

                    print(f"x: {x}        y: {y}")

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