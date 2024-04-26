import pygame

import sys

import random

# settings

COLOR = (255, 255, 255)
WINDOW_HEIGHT = 480
WINDOW_LENGTH = 780
JUMP_COOLDOWN = 1
PIPE_COOLDOWN = 90


class Bird(pygame.sprite.Sprite):

    # class variables
    COLOR = (0, 255, 12)
    JUMP_HEIGHT = -5
    SIZE = 20
    GRAVITY = 0.2

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.y_velocity = 0
        #self.image = pygame.image.load("flappy_bird/images/flappybird.png")
        self.mask = None
    
    def jump(self):
        self.y_velocity = self.JUMP_HEIGHT
    
    def fall(self):
        self.rect.y += self.y_velocity
        self.y_velocity += self.GRAVITY

    def draw(self, window):
        #window.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(window, self.COLOR, self.rect)

    def getYValue(self):
        return self.rect.y
    
    def setYValue(self, yVal):
        self.rect.y = yVal

    def setYVelocity(self, yVelo):
        self.y_velocity = yVelo

    def getRect(self):
        return self.rect



    
class Pipes(pygame.sprite.Sprite):
    #global variables
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    global WINDOW_LENGTH

    #pipe settings
    
    # class variables
    COLOR = (0, 0, 0)
    GAP = 140
    WIDTH = 50
    HEIGHT = 0
    SPEED = 3


    def __init__(self):
        self.HEIGHT = random.randrange(self.GAP + 10, WINDOW_HEIGHT - self.GAP - 10)

        self.rectTop = pygame.Rect(WINDOW_LENGTH - 5, 0, self.WIDTH, self.HEIGHT)
        self.rectBottom = pygame.Rect(WINDOW_LENGTH - 5, 0 + self.HEIGHT + self.GAP, self.WIDTH, 480 - self.HEIGHT)
        self.mask = None
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rectTop)
        pygame.draw.rect(window, self.COLOR, self.rectBottom)
    
    def move(self):
        self.rectTop.x -= self.SPEED
        self.rectBottom.x -= self.SPEED
    
    # getters
    def getXVal(self):
        return self.rectTop.x
    
    def getTopRect(self):
        return self.rectTop
    
    def getBottomRect(self):
        return self.rectBottom




def main():

    #settings
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    global WINDOW_LENGTH
    global PIPE_COOLDOWN
    global JUMP_COOLDOWN

    # initalize variables
    cooldown = 0
    game = False
    obstacles = []
    pipe_cool = 0
    jumping = True

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("flappy bird")

    bird = Bird(50, 150)
    
    window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and jumping == True:
                if event.key == pygame.K_SPACE and cooldown == 0:
                    if game == False:
                        bird.jump()
                        game = True
                        cooldown = JUMP_COOLDOWN
                    
                    else:
                        bird.jump()
                        cooldown = JUMP_COOLDOWN
        
        window.fill(COLOR)  

        # pipe stuff
        # add pipe
        if len(obstacles) < 3 and game and pipe_cool <= 0:
            pipes = Pipes()
            obstacles.append(pipes)
            pipe_cool = PIPE_COOLDOWN

        pipe_cool -= 1

        # iterate through all pipes
        for pipe in obstacles:
            # check if out of bounds
            if pipe.getXVal() < -55:
                obstacles.remove(pipe)
            # draw and move the pipe
            if game and jumping:
                pipe.move()
                pipe.draw(window)

            # check collision and make it so bird cant jump and pipes stop moving
            topRect = pipe.getTopRect()
            bottomRect = pipe.getBottomRect()
            birdRect = bird.getRect()

            if birdRect.colliderect(bottomRect) or birdRect.colliderect(topRect):
                jumping = False



        # bird stuff

        # check if bird is valid
        if bird.getYValue() < -25:
            bird.setYValue(-25)
        
        if bird.getYValue() > WINDOW_HEIGHT - 50:
            bird.setYValue(WINDOW_HEIGHT - 20)
            font = pygame.font.SysFont("Comic Sans MS", 50)
            text_surface = font.render('GAME OVER', False, (255, 0, 0))
            window.blit(text_surface, (WINDOW_LENGTH / 3, WINDOW_HEIGHT / 2.5))
            game = False

        # pipe.draw(window)
        bird.draw(window)

        # check if game has started conditions
        if game and bird.getYValue() < WINDOW_HEIGHT - 50:
            bird.fall()

        
        pygame.display.update()

        if cooldown > 0 :
            cooldown -= 1

if __name__ == "__main__":

    main()
