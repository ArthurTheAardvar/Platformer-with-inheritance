import pygame
import random
from pygame.math import Vector2
pygame.init()
pygame.display.set_caption("Platformer with Inheritance")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

xpos = 100
ypos = 700

LEFT=0
RIGHT=1
UP = 2


keys = [False, False, False] #this list holds whether each key has been pressed

#parent class---------------------------------------
class platform():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
       

    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.pos.x, self.pos.y, 80, 30))

    def move(self):
        pass

    def collide(self):
        pass

   


#child classes inherit all of the parents variables and functions

#child class 1----------------------------------------------
class MovingBlock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.startX = self.pos.x
        self.startY = self.pos.y
        self.direction = 1
       

    def draw(self):
        pygame.draw.rect(screen, (200, 50, 100), (self.pos.x, self.pos.y, 80, 30))

    def move(self):
        if self.direction == 1:
            if self.pos.x < self.startX:
                self.direction*=-1
            else:
                self.pos.x-=1
        else:
            if self.pos.x > self.startX+200:
                self.direction*=-1
            else:
                self.pos.x+=1

    def collide(self):
        pass


class iceBlock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
     


    def draw(self):
        pygame.draw.rect(screen, (50, 50, 200), (self.pos.x, self.pos.y, 80, 30))

    def move(self):
        pass
    def collide(self):
        pass

class trampoline(platform):
    def __init__(self, xpos, ypos, ):
        self.pos = Vector2(xpos,ypos)
       
     

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 80, 30))

    def move(self):
        pass

    def collide(self):
        pass
class breakable(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.isAlive = True
        
        self.life = 2
       
   
        print(self.life)
   
     

    def draw(self):
        if self.life >=2:
            pygame.draw.rect(screen, (0, 0, 255), (self.pos.x, self.pos.y, 80, 30))
           

    def move(self):
        pass

    
        



class Player(breakable):
    def __init__(self, xpos = 100, ypos= 700):
        self.pos = Vector2(xpos,ypos)
        self.vx = 0
        self.vy = 0
        self.isOnGround = False
        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 0 #for left animation, this will need to change for other animations
        self.frameNum = 0
        self.ticker = 0
        self.Link = pygame.image.load("C:/Users/768588/Downloads/link.png") #load your spritesheet
        self.Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
        self.currentplats = 0
        breakable.__init__(self, xpos, ypos)
        
        #super().__init__(life)
     
    def draw(self):
        screen.blit(self.Link, (self.pos.x, self.pos.y-30), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
        #pygame.draw.rect(screen, (100, 200, 100), (self.pos.x, self.pos.y, 20, 40))
    def movement(self, keys):
       
        for event in pygame.event.get(): #quit game if x is pressed in top corner
           
     
            if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=True

                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=True

                elif event.key == pygame.K_UP:
                    keys[UP]=True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=False

                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]= False

                elif event.key == pygame.K_UP:
                    keys[UP]=False

        if keys[LEFT]==True:
            self.vx=-3
           

        elif keys[RIGHT]==True:
            self.vx=3
         
        else:
            self.vx = 0

        if keys[UP] == True and self.isOnGround == True: #only jump when on the ground
            #print("Up is being pressed")
            self.vy = -8
            self.isOnGround = False
       
        if self.isOnGround == False:
            self.vy+=.2 #notice this grows over time, aka ACCELERATION

        if self.pos.y > 800:
            self.isOnGround = True
            self.vy = 0
            self.pos.y = 800

       

        if self.pos.y <= 0:
            self.vy+= 10
 
        if self.currentplats ==4:
            self.vy -= 3

        if self.currentplats == 2:
            num = random.randrange(1,3)
            if num == 1:
                self.vx +=3
            else:
                self.vx -=3

        while self.currentplats ==5:
            self.life -=1
            if self.life >= 2:
               breakable.draw(self)
            else:
               print("its gone😁")
            print("colliding")
            print(self.life)
           
           


       
   
        self.pos +=(self.vx, self.vy)
       

    def collision(self, plats):
        colliding = False

        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > 750:
            self.pos.x = 750

        if self.pos.y > 760:
            colliding = True
            self.isOnGround = True
            self.pos.y = 760
       
        playerrect = pygame.rect.Rect(self.pos, (self.frameWidth, self.frameHeight))
        for plats in plats:
            platrect = pygame.rect.Rect(plats.pos.x, plats.pos.y+30, 80, 30)
            if playerrect.colliderect(platrect):
                colliding = True
                if isinstance(plats, iceBlock):
                    self.currentplats = 2
                elif isinstance(plats, MovingBlock):
                    self.currentplats = 3
                elif isinstance(plats, trampoline):
                    self.currentplats = 4
                elif isinstance(plats, breakable):
                    self.currentplats = 5
               
                else:
                    self.currentplats = 1
           
        if colliding:
            self.isOnGround = True
            if self.vy >0:
                self.vy = 0
                self.pos.y -= 1
           

        else:
            self.currentplats = 0
            self.isOnGround = False

       
       
       
    def animate(self):
        if self.vx < 0: #left animation
            self.RowNum = 0
            self.ticker+=1

            if self.ticker%5==0:
                self.frameNum+=1
               
            if self.frameNum>7:
                self.frameNum = 0

        if self.vx > 0:
            self.RowNum = 1
            self.ticker+=1
            if self.ticker%5==0:
                self.frameNum+=1
               
            if self.frameNum>7:
                self.frameNum = 0

       

       

        return self.ticker
   
       


plats = []

for i in range(3):
    plats.append(iceBlock(random.randrange(50, 750), random.randrange(50, 750)))

for i in range(3):
    plats.append(platform(random.randrange(50, 750), random.randrange(50, 750)))

for i in range(3):
    plats.append(MovingBlock(random.randrange(50, 750), random.randrange(50, 750)))

for i in range(3):
    plats.append(trampoline(random.randrange(50, 750), random.randrange(50, 750)))
for i in range(3):
    plats.append(breakable(random.randrange(50, 750), random.randrange(50, 750)))

player = Player(xpos, ypos)

while(1): #gameloop-----------------------------------------
   
    clock.tick(60) #FPS
    
    #print(mousePos)
    player.movement(keys)
   
 

    for i in range(len(plats)):
        plats[i].move()
        plats[i].collide()



#render section-----------------------------------
    screen.fill((0,0,0))
    player.draw()
 
    for i in range (len(plats)):
        plats[i].draw()

    player.collision(plats)
    player.animate()
    pygame.display.flip()

pygame.quit()
