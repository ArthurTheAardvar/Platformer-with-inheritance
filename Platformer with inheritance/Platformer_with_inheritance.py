import pygame
import random
pygame.init()
pygame.display.set_caption("Platformer with Inheritance")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False
isOnGround = False
xpos = 100
ypos = 620
mousePos = (xpos, ypos)

LEFT=1
RIGHT=2
UP = 3



direction = [LEFT == 1, RIGHT==2, UP == 3]

keys = [False, False, False, False] #this list holds whether each key has been pressed

#parent class---------------------------------------
class platform():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.xpos, self.ypos, 80, 30))

    def move(self):
        pass


#child classes inherit all of the parents variables and functions

#child class 1----------------------------------------------
class MovingBlock(platform):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        self.direction = 1
        

    def draw(self):
        pygame.draw.rect(screen, (200, 50, 100), (self.xpos, self.ypos, 80, 30))

    def move(self):
        if self.direction == 1:
            if self.xpos < self.startX:
                self.direction*=-1
            else:
                self.xpos-=1
        else:
            if self.xpos > self.startX+200:
                self.direction*=-1
            else:
                self.xpos+=1



class iceBlock(platform):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos


    def draw(self):
        pygame.draw.rect(screen, (50, 50, 200), (self.xpos, self.ypos, 80, 30))
        

        



class Player():
    def __init__(self, xpos, ypos, direction):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = 0
        self.vy = 0
        self.isOnGround = True
        self.direction = direction
        self.frameWidth = 50
        self.frameHeight = 75
        self.RowNum = 0 #for left animation, this will need to change for other animations
        self.frameNum = 0
        self.ticker = 0
        self.Link = pygame.image.load("C:/Users/768588/Pictures/link.png") #load your spritesheet
        self.Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
        
    def draw(self):
        screen.blit(self.Link, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))

    def movement(self):
        

        if keys[LEFT]==True:
            self.vx=-3
            self.direction = LEFT

        elif keys[RIGHT]==True:
            self.vx=3
            self.direction = RIGHT
          #turn off velocity
        else:
            self.vx = 0
            
        #JUMPING

        if keys[UP] == True and self.isOnGround == True: #only jump when on the ground
            #print("Up is being pressed")
            self.vy = -8 
            self.isOnGround = False
            self.direction = UP
  

        if self.ypos > 700:
            self.isOnGround = True
            self.vy = 0
            self.ypos = 700

        
        

    def collision(self):
        
           

        else:
            isOnGround = False

        if self.isOnGround == False:
            self.vy+=.2 #notice this grows over time, aka ACCELERATION


        self.xpos+=self.vx
        self.ypos+=self.vy
        #print(self.xpos, self.ypos)
        
        
    def animate(self):
        if self.vx < 0: #left animation
            self.RowNum = 0
        # ticker is a spedometer. We don't want Link animating as fast as the processor can process! Update Animation frame each time ticker goes over
            self.ticker+=1

            if self.ticker%5==0:
                self.frameNum+=1
                #if we are over the number of frames in our sprite, reset to 0.
            if self.frameNum>7:
                self.frameNum = 0
        if self.vx > 0:
            self.RowNum = 1
            self.ticker+=1
            if self.ticker%5==0:
                self.frameNum+=1
                #if we are over the number of frames in our sprite, reset to 0.
            if self.frameNum>7:
                self.frameNum = 0

        

        

        return self.ticker
    
        


plats = []

for i in range(1):
    plats.append(iceBlock(100, 700))

for i in range(1):
    plats.append(platform(300, 630))

for i in range(1):
    plats.append(MovingBlock(600, 700))

player = Player(xpos, ypos, direction)
while(1): #gameloop-----------------------------------------
    
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
            if event.type == pygame.QUIT:
                gameover = True
      
            if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=True

                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=True

                elif event.key == pygame.K_UP:
                    keys[UP]=True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=False

                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]= False

                elif event.key == pygame.K_UP:
                    keys[UP]=False

            if event.type == pygame.MOUSEMOTION:
                mousePos = event.pos

      
                
    
    #print(mousePos)
    player.movement()
    player.collision()
    player.animate()
    

    for i in range(len(plats)):
        plats[i].move()



#render section-----------------------------------
    screen.fill((0,0,0))
    player.draw()
    for i in range (len(plats)):
        plats[i].draw()


    pygame.display.flip()

pygame.quit()