import pygame as pg
import sys
import pygame.font
import random
from pygame.math import Vector2
pygame.init()

mxpos = 0
mypos = 0
mousePos = (mxpos, mypos)
keys = [False, False, False] #this list holds whether each key has been pressed

LEFT = 1
RIGHT = 2
UP = 3
#platform class-------------------------------------------------------------
#parent class---------------------------------------
class platform():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
       

    def draw(self, screen):
        pg.draw.rect(screen, (100, 50, 100), (self.pos.x, self.pos.y, 80, 30))

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
       

    def draw(self, screen):
        pg.draw.rect(screen, (200, 50, 100), (self.pos.x, self.pos.y, 80, 30))

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
     


    def draw(self, screen):
        pg.draw.rect(screen, (50, 50, 200), (self.pos.x, self.pos.y, 80, 30))

    def move(self):
        pass
    def collide(self):
        pass

class trampoline(platform):
    def __init__(self, xpos, ypos, ):
        self.pos = Vector2(xpos,ypos)
       
     

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 80, 30))

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
   
     

    def draw(self, screen):
        if self.life >=2:
            pygame.draw.rect(screen, (0, 0, 255), (self.pos.x, self.pos.y, 80, 30))
           

    def move(self):
        pass

#goal class-------------------------------------------------------------
class goal():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        

    def draw(self, screen):
        pg.draw.rect(screen, (250, 0, 0), (self.xpos, self.ypos, 20,20))

goals = [] #you can have more than one in each level :)



#--------------------------------------------------------------------------------

#player class
class Player():
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
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.font = pg.font.Font(None, 36)
      

    def draw(self, screen):
        screen.blit(self.Link, (self.pos.x, self.pos.y-30), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
        #pygame.draw.rect(screen, (100, 200, 100), (self.pos.x, self.pos.y, 20, 40))
    
       
       
    def move_left(self):
        self.vx = -5
    
       
    def move_right(self):
        self.vx = 5
      
        print("Rights being pressed")
       
    def stop(self):
        self.vx = 0
        
       
    def jump(self):
        if self.isOnGround == True or self.isOnGround == False:
            self.vy = -8
            print("Up being pressed")
       
    def update(self, platforms):
        
        

        self.pos +=(self.vx, self.vy)
       
        if self.collision(platforms):
            self.isOnGround = True
            self.vy = 0

        else:
            self.isOnGround = False
       
        if self.pos.y > 760:
            self.isOnGround = True
            self.pos.y = 0
            self.pos.y = 760
           
    
           
        for goal in goals:
            if self.pos.x + 10 >= goal.xpos and self.pos.x <= goal.xpos + 20:
                if self.pos.y + 30 >= goal.ypos and self.pos.y + 30 <= goal.ypos + 20:
                    print("goal hit!")
                    self.pos.x = 100
                    self.pos.y = 700
                    return True  # Change state when player touches a red square
           
    
       
            



        
    
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
       
       
p1 = Player(100, 700)
plats = []
#--------------------------------------------------------------------------------
#the parent class!
class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.font = pg.font.Font(None, 36)
        self.keys = [False, False, False]
        self.UP = 2
        self.LEFT = 0
        self.RIGHT = 1
       
    def get_event(self, event):
        
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                p1.move_left()

            elif event.key == pygame.K_RIGHT:
                p1.move_right()

            elif event.key == pygame.K_UP:
                p1.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1.stop()

            elif event.key == pygame.K_RIGHT:
                p1.stop()

            elif event.key == pygame.K_UP:
                p1.stop()

        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = False

#--------------------------------------------------------------------------------
class End(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelOne'
       
    def cleanup(self):
        print('cleaning up End state stuff')
       
    def startup(self):
        print('starting End state stuff')

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)==True:
            self.done = True
       
    def draw(self, screen):
        screen.fill((0,0,80))
        text = self.font.render("You Win!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 400))  
        screen.blit(text, text_rect)

#--------------------------------------------------------------------------------
class titleScreen(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelOne'

    def cleanup(self):
        print('cleaning up title stuff')
        plats.clear();

    def draw(self, screen):
        screen.fill((0,0,0))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
        for i in range (len(goals)):
            goals[i].draw(screen)
        text = self.font.render("Really Amazing Cool Game", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 400))  
        screen.blit(text, text_rect)

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)==True:
            self.done = True
        
            

    def startup(self):
        print('Title Screen')
        plats.append(platform(200, 700))
        plats.append(platform(200, 600))
        plats.append(platform(300, 500))
        plats.append(platform(400, 400))
        plats.append(platform(500, 300))
        plats.append(trampoline(600, 200))
        plats.append(platform(700, 100))
    
        goals.append(goal(750, 100))


    

class LevelOne(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelTwo'
       
       
    def cleanup(self):
        print('cleaning up Level 1 stuff')
        plats.clear();
       
    def startup(self):
        print('Level 1!')
        plats.append(platform(200, 400))
        plats.append(platform(500, 200))
        plats.append(platform(500, 300))
        plats.append(platform(100, 200))
        plats.append(platform(200, 700))
        plats.append(platform(200, 600))
        plats.append(platform(300, 500))
        plats.append(platform(400, 400))

        goals.append(goal(750, 100))
       

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)==True:
            self.done = True
            
       
    def draw(self, screen):
        screen.fill((0,0,0))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
        for i in range (len(goals)):
            goals[i].draw(screen)
        text = self.font.render("Level 1", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 20))  
        screen.blit(text, text_rect)
       
       
#--------------------------------------------------------------------------------

class LevelTwo(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'LevelThree'
       
    def cleanup(self):
        print('cleaning up Level 2 stuff')
        plats.clear();
       
    def startup(self):
        print('Level 2!')
        plats.append(platform(100, 500))
        plats.append(platform(400, 300))
        plats.append(platform(400, 600))
        plats.append(platform(600, 700))
        goals.append(goal(750, 100))

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)== True:
            self.done = True
            
       
    def draw(self, screen):
        screen.fill((0,0,255))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
        for i in range (len(goals)):
            goals[i].draw(screen)
        text = self.font.render("Level 2", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 20))  
        screen.blit(text, text_rect)

class LevelThree(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'End'
       
    def cleanup(self):
        print('cleaning up Level 3 stuff')
        plats.clear();
       
    def startup(self):
        print('Level 3!')
        plats.append(platform(100, 500))
        plats.append(platform(400, 300))
        plats.append(platform(400, 600))
        plats.append(platform(600, 700))
        goals.append(goal(750, 100))

    def update(self, screen, dt):
        self.draw(screen)
        if p1.update(plats)== True:
            self.done = True
            
       
    def draw(self, screen):
        screen.fill((0,0,255))
        p1.draw(screen)
        for i in range (len(plats)):
            plats[i].draw(screen)
        for i in range (len(goals)):
            goals[i].draw(screen)
        text = self.font.render("Level 3", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 20))  
        screen.blit(text, text_rect)
#--------------------------------------------------------------------------------      
class Control:
    def __init__(self, **settings): # ** denotes a KWARG, which lets you have an unknown num of parameters
        self.__dict__.update(settings) #double underscore helps to avoid naming conflicts in subclasses
        self.done = False
        self.screen = pg.display.set_mode(settings["size"])
        self.clock = pg.time.Clock()
       
       
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name] #state has been set to an OBJECT
       
       
    def flip_state(self):
        self.state.done = False #we are referencing the variable of whatever OBJECT is in "state"
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
       
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
       
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
           
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(settings["fps"])/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
 
#--------------------------------------------------------------------------------
#"main"
           
#a dictionary containing the settings
settings = {
    'size':(800,800),
    'fps' :60
}

#a dictionary containing all the different states available
state_dict = {
    'End': End(),
    'Title': titleScreen(),
    'LevelOne': LevelOne(),
    'LevelTwo': LevelTwo(),
    'LevelThree': LevelThree()
}

#------------------------------------
#instantiate a control object named "app"
#after running this constructor, "app" will have 4 variables:
#a copy of the settings dictionary, a boolean named "done" set to False,
#a screen variable holding the pygame display, and a clock variable
app = Control(**settings)
#------------------------------------

#------------------------------------
#the setup_states function passes in the dictionary of available states
#and also sets what the begnning state will be
app.setup_states(state_dict, 'Title')
app.state.startup() #call startup for the initial state, Level One
#------------------------------------

#------------------------------------
app.main_game_loop() #OMG GAME LUP!

pg.quit()
sys.exit()