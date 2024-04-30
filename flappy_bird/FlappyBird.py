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
    SIZE = 15
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
        window.blit(self.image, (self.rect.x - 10, self.rect.y - 5))
        #pygame.draw.rect(window, self.COLOR, self.rect)

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
        self.HEIGHT = random.randrange(10, WINDOW_HEIGHT - self.GAP + 10)
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
    
    def getWidth(self):
        return self.WIDTH

def main():

    #settings
    global WINDOW_HEIGHT
    global WINDOW_LENGTH
    global WINDOW_LENGTH
    global PIPE_COOLDOWN
    global JUMP_COOLDOWN

    # initalize pygame stuff
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    # initalize variables
    cooldown = 0
    game = False
    obstacles = []
    pipe_cool = 0
    jumping = True
    score = 0
    scoreFont = pygame.font.SysFont("Comic Sans MS", 20)
    current_pipe = 0

    BIRD_HEIGHT = 150

    pygame.display.set_caption("flappy bird")

    # create bird
    bird = Bird(50, BIRD_HEIGHT)
    
    # create window
    window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

    while True:
        # update screen and make 60 fps
        clock.tick(60)
        window.fill(COLOR)  
    
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # jump
                if event.key == pygame.K_SPACE and cooldown == 0 and jumping == True:
                    if game == False:
                        bird.jump()
                        game = True
                        cooldown = JUMP_COOLDOWN

                        # add first pipe
                        pipes = Pipes()
                        obstacles.append(pipes)
                    
                    else:
                        bird.jump()
                        cooldown = JUMP_COOLDOWN
                
                # restart
                if event.key == pygame.K_r:
                    print("here")
                    jumping = True
                    bird.setYValue(BIRD_HEIGHT)
                    score = 0

                    for i in range(0, len(obstacles)):
                        obstacles.pop()


        
        # pipe stuff
        # add pipe
        

        if len(obstacles) < 3 and game and obstacles[current_pipe].getXVal() <= (int) (WINDOW_LENGTH / 3):
            pipes = Pipes()
            obstacles.append(pipes)
            pipe_cool = PIPE_COOLDOWN

            if current_pipe < 3:
                current_pipe += 1

        pipe_cool -= 1

        # iterate through all pipes
        removePipe = []
        indx = 0
        for pipe in obstacles:
            # check if out of bounds
            if pipe.getXVal() < - pipe.getWidth():
                removePipe.append(indx)
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
            indx += 1

        # remove pipe
        removed = 0
        for indx in removePipe:
            obstacles.pop(indx - removed)
            score += 1
            removed += 1

        # bird stuff

        # check if bird is is in game
        if bird.getYValue() < 0:
            bird.setYValue(0)
        
        if bird.getYValue() >= WINDOW_HEIGHT - 10:
            bird.setYValue(WINDOW_HEIGHT - 10)
            gameOverFont = pygame.font.SysFont("Comic Sans MS", 50)
            text_surface = gameOverFont.render('GAME OVER', False, (255, 0, 0))
            window.blit(text_surface, (WINDOW_LENGTH / 3, WINDOW_HEIGHT / 2.5))
            jumping = False
            game = False

        # check if game has started conditions
        if game and bird.getYValue() < WINDOW_HEIGHT - 10:
            bird.fall()

        # draw stuff
        bird.draw(window)
        
        # display font
        stringScore = str(score)
        textScore = scoreFont.render("score: " + stringScore, 1, (125, 125, 125))
        window.blit(textScore, (0, 0))

        pygame.display.update()

        if cooldown > 0 :
            cooldown -= 1

if __name__ == "__main__":

    main()
