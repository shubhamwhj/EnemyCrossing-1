import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=300
screen = pygame.display.set_mode((width,height))
  
start=rect= pygame.Rect(0,0,50,300)
finish=rect= pygame.Rect(350,0,50,300)

score=0
score_font=pygame.font.Font('freesansbold.ttf', 25)

class Player:
    speed=0
    g=0.5
    rect= pygame.Rect(10,150,20,20)

    def moveRight(self):
        self.speed=3
        
    def moveLeft(self):
        self.speed=0
        
    def display(self):
        self.rect.x+=self.speed
        pygame.draw.rect(screen,(250,150,50),self.rect)

class Enemy:
   def __init__(self, x, y):
       self.rect= pygame.Rect(x,y,20,20)
       
   def display(self):  
        pygame.draw.rect(screen,(250,10,50),self.rect)
            
    
state="play"
player= Player()
enemy1=Enemy(100,0) 
enemy2=Enemy(160,280) 
enemy3=Enemy(220,0) 
enemy4=Enemy(280,280)
while True:    
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            if event.key == pygame.K_RIGHT:
                player.moveRight()
               
    if state=="play":          

        pygame.draw.rect(screen,(0,0,200),start)
        pygame.draw.rect(screen,(0,200,000),finish)
        enemy1.display()
        enemy2.display()
        enemy3.display()
        enemy4.display()
        player.display()
        
    if state=="win":
        over_text=score_font.render("Winner!", False, (255,255,0))  
        screen.blit(over_text,[125,125]) 
    
    if state=="over":
        over_text=score_font.render("Game Over", False, (255,255,0))  
        screen.blit(over_text,[125,125]) 
      
    if player.rect.x>350:
        state="win"

    pygame.display.update() 
    clock.tick(30) 
    
    
    
    
    

 