import time
import pygame
import numpy as np
from GUIModules import Constans


def update(screen, cells, size, withProgress=False):
    updatedCells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = Constans.colorBg if cells[row, col] == 0 else Constans.colorAlive

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if withProgress:
                    color = Constans.colorDie

            elif 2 <= alive <= 3:
                updatedCells[row, col] = 1
                if withProgress:
                    color = Constans.colorAlive

        else:
            if alive == 3:
                updatedCells[row, col] = 1
                if withProgress:
                    color = Constans.colorAlive

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updatedCells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(Constans.colorGrid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(Constans.colorGrid)

        if running:
            cells = update(screen, cells, 10, withProgress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == '__main__':
    main()
