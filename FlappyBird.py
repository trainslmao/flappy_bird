import pygame

import sys

import random

class Bird(pygame.sprite.Sprite):

    # class variables
    COLOR = (0, 0, 0)
    JUMP_HEIGHT = -6
    SIZE = 30
    GRAVITY = 0.2

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.y_velocity = 0
        self.mask = None
    
    def jump(self):
        self.y_velocity = self.JUMP_HEIGHT
    
    def fall(self):
        self.rect.y += self.y_velocity
        self.y_velocity += self.GRAVITY

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)

    def getYValue(self):
        return self.rect.y
    
    def setYValue(self, yVal):
        self.rect.y = yVal

    def setYVelocity(self, yVelo):
        self.y_velocity = yVelo
    
class Pipes(pygame.sprite.Sprite):
    # class variables
    COLOR = (0, 225, 0)
    GAP = 50
    WIDTH = 30

    def __init__(self, x):
        self.rect = pygame.Rect(x, 0, (x, 0, self.WIDTH, self.GAP))
        self.mask = None
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)







def main():

    # settings

    COLOR = (255, 255, 255)
    WINDOW_HEIGHT = 480
    WINDOW_LENGTH = 780
    JUMP_COOLDOWN = 1

    # initalize variables
    cooldown = 0
    start = False
    game = True

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("flappy bird")

    bird = Bird(50, 150)
    #pipe = Pipes(400)

    window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))


    

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cooldown == 0 and bird.getYValue() > 0 and game == True:
                    if start != True:
                        bird.jump()
                        start = True
                        cooldown = JUMP_COOLDOWN
                    
                    else:
                        bird.jump()
                        cooldown = JUMP_COOLDOWN
        
        window.fill(COLOR)  

        # check game conditions
        if start:
            bird.fall()

        if bird.getYValue() < 0:
            bird.setYValue(0)
        
        if bird.getYValue() > WINDOW_HEIGHT:
            bird.setYValue(WINDOW_HEIGHT - 10)
            font = pygame.font.SysFont("Comic Sans MS", 50)
            text_surface = font.render('GAME OVER', False, (255, 0, 0))
            window.blit(text_surface, (WINDOW_LENGTH / 3, WINDOW_HEIGHT / 2.5))

        #pipe.draw(window)
        bird.draw(window)

        pygame.display.update()

        if cooldown > 0 :
            cooldown -= 1



if __name__ == "__main__":

    main()