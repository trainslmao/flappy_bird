import pygame

import sys

import random

# settings

COLOR = (255, 255, 255)
WINDOW_HEIGHT = 480
WINDOW_LENGTH = 780
JUMP_COOLDOWN = 1




class Bird(pygame.sprite.Sprite):

    # class variables
    COLOR = (0, 0, 0)
    JUMP_HEIGHT = -5
    SIZE = 50
    GRAVITY = 0.2

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.y_velocity = 0
        self.image = pygame.image.load("flappy_bird/images/flappybird.png")
        self.mask = None
    
    def jump(self):
        self.y_velocity = self.JUMP_HEIGHT
    
    def fall(self):
        self.rect.y += self.y_velocity
        self.y_velocity += self.GRAVITY

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def getYValue(self):
        return self.rect.y
    
    def setYValue(self, yVal):
        self.rect.y = yVal

    def setYVelocity(self, yVelo):
        self.y_velocity = yVelo
    
class Pipes(pygame.sprite.Sprite):
    #global variables
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    global WINDOW_LENGTH

    #pipe settings
    

    # class variables
    COLOR = (0, 225, 0)
    GAP = 100
    WIDTH = 50
    HEIGHT = random.randrange(50, 590)
    SPEED = 5


    def __init__(self):
        self.rectTop = pygame.Rect(WINDOW_LENGTH - 5, 0, self.WIDTH, self.HEIGHT)
        self.rectBottom = pygame.Rect(WINDOW_LENGTH - 5, 0 + self.HEIGHT + self.GAP, self.WIDTH, 480 - self.HEIGHT)
        self.mask = None
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rectTop)
        pygame.draw.rect(window, self.COLOR, self.rectBottom)
    
    def move(self):
        self.rectTop.x -= self.SPEED
        self.rectBottom.x -= self.SPEED
    
    def kill(self) -> None:
        return super().kill()
    
    def getXVal(self):
        return self.rectTop.x







def main():

    #settings
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    global WINDOW_LENGTH

    # initalize variables
    cooldown = 0
    start = False
    game = True
    obstacles = []

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cooldown == 0 and game == True:
                    if start != True:
                        bird.jump()
                        start = True
                        cooldown = JUMP_COOLDOWN
                    
                    else:
                        bird.jump()
                        cooldown = JUMP_COOLDOWN
        
        window.fill(COLOR)  

        # pipe stuff
        # add pipe
        if len(obstacles) < 3:
            print("here")
            pipes = Pipes()
            obstacles.append(pipes)

        # iterate through all pipes
        for pipe in obstacles:
            # check if out of bounds
            if pipe.getXVal() < 0:
                pipe.kill()

            # draw and move the pipe
            pipe.move()
            pipe.draw(window)


        # bird stuff

        # check if bird is valid
        if bird.getYValue() < -25:
            bird.setYValue(-25)
        
        if bird.getYValue() > WINDOW_HEIGHT - 50:
            bird.setYValue(WINDOW_HEIGHT - 20)
            font = pygame.font.SysFont("Comic Sans MS", 50)
            text_surface = font.render('GAME OVER', False, (255, 0, 0))
            window.blit(text_surface, (WINDOW_LENGTH / 3, WINDOW_HEIGHT / 2.5))

        # pipe.draw(window)
        bird.draw(window)

        # check if game has started conditions
        if start and bird.getYValue() < WINDOW_HEIGHT - 50:
            bird.fall()

        
        pygame.display.update()

        if cooldown > 0 :
            cooldown -= 1



if __name__ == "__main__":

    main()
