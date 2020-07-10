import pygame
import math
#import keyboard
import sys
from math import sqrt




# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

#=============================================
x=300
y=250
newX=0
newY=0

newX1=0
newY1=0

newX2=0
newY2=0

newX3=0
newY3=0

x1=200
y1=200
x1_s=0
y1_s=0

rad=200
angle=0
#=============================================
ball1=[x1,y1]


#===================проба===================






#=============================================




pi=3.14
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
    screen.fill(WHITE)
    
    pygame.draw.circle(screen, BLACK,ball1,5)


    pygame.draw.circle(screen, GREEN,[300,250],5)
    pygame.draw.line(screen,RED,[newX,newY],[newX1,newY1], 5)    
    pygame.draw.line(screen,RED,[newX1,newY1],[newX2,newY2], 5)
    pygame.draw.line(screen,RED,[newX2,newY2],[newX3,newY3], 5)
    pygame.draw.line(screen,RED,[newX3,newY3],[newX,newY], 5)
    
    #pygame.draw.polygon(screen, RED, [[newX,newY],[newX1,newY1],[newX2,newY2],[newX3,newY3]], 10)
    #===============проверка линий===========================
    pygame.draw.line(screen,BLACK,[newX,newY],[x1,y1], 1)
    pygame.draw.line(screen,BLACK,[x1,y1],[newX1,newY1], 1)
    #pygame.draw.line(screen,BLACK,[newX,newY],[newX1,newY1], 5)
    

    #========================================================
    newX=x+rad*math.cos(angle)
    newY=y+rad*math.sin(angle)

    newX1=x+rad*math.cos(angle+45.55)
    newY1=y+rad*math.sin(angle+45.55)

    newX2=x+rad*math.cos(angle+91.1)
    newY2=y+rad*math.sin(angle+91.1)

    newX3=x+rad*math.cos(angle+136.65)
    newY3=y+rad*math.sin(angle+136.65)

   

    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            angle-=0.01
        if event.key == pygame.K_RIGHT:
            angle+=0.01
        if event.key == pygame.K_a:
            x1-=1
        if event.key == pygame.K_d:
            x1+=1
        if event.key == pygame.K_w:
            y1-=1
        if event.key == pygame.K_s:
            y1+=1
    
    
    
 #=============================================================
    
    ball1=[x1+x1_s,y1+y1_s]
 #=============================================================
    xy=sqrt(((newX-newX1)**2)+((newY-newY1)**2))
    xc=sqrt(((x1-newX1)**2)+((y1-newY1)**2))
    cy=sqrt(((newX-x1)**2)+((newY-y1)**2))
    cosA=(((xy**2)+(xc**2))-(cy**2))/(2*xy*xc)
    
    xd=xc*cosA
    dc=sqrt((xc**2)-(xd**2))
    yd1=sqrt(dc)
    
  #=====================================================
    xx=newX1+xd
    yy=y1+yd1
    
    #xx=x+rad*math.cos(angle+45.55)
    #yy=y+rad*math.sin(angle+45.55)
    
    pygame.draw.line(screen,BLUE,[x1,y1],[xx,yy], 1)
    print(xd,yd1)
        
    
    
 #=============================================================

    #angle+=0.03
   

    # background image.
    
    
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(100)
 
# Close the window and quit.
pygame.quit()