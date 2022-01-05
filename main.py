import pygame
from pygame.constants import WINDOWSIZECHANGED

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500


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

    while running:
        drawGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()