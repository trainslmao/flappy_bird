import pygame

import sys

import random

class Bird(pygame.sprite.Sprite):

    # class variables
    COLOR = (0, 0, 0)
    JUMP_HEIGHT = -6
    SIZE = 50
    GRAVITY = 0.2

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.y_velocity = 0
        self.image = pygame.image.load("images/flappybird.jpg")
        self.mask = None
    
    def jump(self):
        self.y_velocity = self.JUMP_HEIGHT
    
    def fall(self):
        self.rect.y += self.y_velocity
        self.y_velocity += self.GRAVITY

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
    



COLOR = (255, 255, 255)

pygame.init()

pygame.display.set_caption("flappy bird")

bird = Bird(50, 50)

window = pygame.display.set_mode((640, 480))





def main(window):

    # initalize variables
    cooldown = 0

    # game settings
    JUMP_COOLDOWN = 15

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cooldown == 0:
                    bird.jump()
                    cooldown = JUMP_COOLDOWN
        
        window.fill(COLOR)  

        bird.fall()
        
        bird.draw(window)

        pygame.display.update()

        if cooldown > 0 :
            cooldown -= 1



if __name__ == "__main__":
    main(window)
