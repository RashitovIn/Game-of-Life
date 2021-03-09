import pygame
import random
import sys
import numpy as np

class Game:
    screen = None

    def count_n(self, x, y):
        count = 0
        for i in range(-1 , 2):
            for j in range(-1 , 2):
                col = (x + i + self.cols ) % self.cols
                row = (y + j + self.rows ) % self.rows
                is_self = col == x and row == y
                has_life = self.field[col, row]
                if (has_life and not is_self):
                    count += 1
        return count


    def __init__(self, height, width, size_block):
        pygame.init()
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.size_block = size_block


        self.cols = self.width // self.size_block
        self.rows = self.height // self.size_block
        self.field = np.array([[False] * self.rows] *  self.cols)
        for x in range(self.cols):
            for y in range(self.rows):
                state = random.randint(0, 1) == 0
                self.field[x, y] = state
        #self.field[0][1] = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(print(" Выход "))

            new_field = np.array([[False] * self.rows] * self.cols)

            for x in range(self.cols):
                for y in range(self.rows):
                    #print(self.field[x][y])

                    nc = self.count_n(x, y)
                    print(nc)
                    has_life = self.field[x, y]
                    if (not has_life and nc == 3):
                        new_field[x, y] = True
                    elif (has_life and (nc < 2 or nc > 3)):
                        new_field[x, y] = False
                    else:
                        new_field[x, y] = self.field[x, y]
                    if has_life:
                        #print(y, x)
                        #print(self.field)
                        pygame.draw.rect(self.screen, (224, 0, 0), ((x + 1) * self.size_block, (y + 1) * self.size_block,  self.size_block - 2,  self.size_block - 2))
            self.field = new_field
            pygame.display.flip()
            #pygame.display.update()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
if __name__ == "__main__":
    game = Game(1000,1000,10)