import pygame

import sys

import random

class Bird(pygame.sprite.Sprite):

    # class variables
    COLOR = (0, 0, 0)
    JUMP_HEIGHT = -1

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.y_velocity = 0
        self.mask = None
    
    def jump(self):
        self.y_velocity += self.JUMP_HEIGHT
    
    def fall(self):
        self.rect.y += self.y_velocity
        self.y_velocity += 0.1

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
    



COLOR = (255, 255, 255)

pygame.init()

pygame.display.set_caption("flappy bird")

bird = Bird(50, 50)

window = pygame.display.set_mode((640, 480))


def main(window):
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        window.fill(COLOR)  

        bird.fall()
        
        bird.draw(window)

        pygame.display.update()



if __name__ == "__main__":
    main(window)
