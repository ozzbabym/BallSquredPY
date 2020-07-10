import pygame
import math
import sys
import os
from math import sqrt
import random
import py2exe
from pygame import font






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

xq=300
yq=250
gameover=[xq,yq]
#=============================================
ball1=[x1,y1]
ball2=False
ball3=False
ball4=False
ball5=False


ygolglob=angle

score=0

#======================================

xf=random.randint(230,370)
yf=random.randint(230,370)


#==================проба======================
font1=0
text1=0
font2=0
text2=0
font3=0
text3=0
font4=0
text4=0

#=============================================
def Gameover():
    font1 = pygame.font.SysFont(None, 25)
    text1 = font1.render("Game Over",True,BLACK)
    screen.blit(text1, [250,300])

def Try():
    font2 = pygame.font.SysFont(None, 25)
    text2 = font2.render("If you want to try, press 'R'",True,BLACK)
    screen.blit(text2, [200,450])
    
def Score():
    font4 = pygame.font.SysFont(None, 25)
    text4 = font4.render("Score: "+str(score),True,BLACK)
    screen.blit(text4, [400,30])    
    
def Start():
    font3 = pygame.font.SysFont(None, 25)
    text3 = font3.render("Start or Restart, press 'R'",True,BLACK)
    screen.blit(text3, [30,30])   
    

pi=3.14
pygame.init()
pygame.font.init()

# Set the width and height of the screen [width, height]
size = (600, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ball Squared")


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
    pygame.draw.circle(screen, BLACK,ball1,7)
    pygame.draw.circle(screen, GREEN,gameover,5)

    #pygame.draw.line(screen,BLACK,gameover,ball1,1)


    gover=sqrt(((int(x1)-int(xq))**2)+((int(y1)-int(yq))**2))
    if gover<10 or x1<0 or y1<0 or x1>700 or y1>500:
        ball2=False
        ball3=False
        ball4=False
        ball5=False


        Gameover()

        Try()



    pygame.draw.line(screen,BLUE,[newX,newY],[newX1,newY1], 5)
    pygame.draw.line(screen,RED,[newX1,newY1],[newX2,newY2], 5)
    pygame.draw.line(screen,RED,[newX2,newY2],[newX3,newY3], 5)
    pygame.draw.line(screen,RED,[newX3,newY3],[newX,newY], 5)

    Score()

    Start()


    #pygame.draw.polygon(screen, RED, [[newX,newY],[newX1,newY1],[newX2,newY2],[newX3,newY3]], 10)
    #===============проверка линий===========================
    #pygame.draw.line(screen,BLACK,[newX,newY],[x1,y1], 1)
    #pygame.draw.line(screen,BLACK,[x1,y1],[newX1,newY1], 1)
    #pygame.draw.line(screen,BLACK,[newX,newY],[newX1,newY1], 5)
    #pygame.draw.line(screen,BLACK,[x1,y1],[newX2,newY2], 1)
    #pygame.draw.line(screen,BLACK,[x1,y1],[newX3,newY3], 1)

    #========================================================
    newX=int(x+rad*math.cos(ygolglob))
    newY=int(y+rad*math.sin(ygolglob))

    newX1=int(x+rad*math.cos(ygolglob+1.57))
    newY1=int(y+rad*math.sin(ygolglob+1.57))

    newX2=int(x+rad*math.cos(ygolglob+3.14))
    newY2=int(y+rad*math.sin(ygolglob+3.14))

    newX3=int(x+rad*math.cos(ygolglob+4.71))
    newY3=int(y+rad*math.sin(ygolglob+4.71))

    if ygolglob>=0.785:
        ygolglob=-0.785
    elif ygolglob<=-0.785:
         ygolglob=0.785















    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            ygolglob-=0.005
        if event.key == pygame.K_RIGHT:
            ygolglob+=0.005
        if event.key == pygame.K_a:
            x1-=1
        if event.key == pygame.K_d:
            x1+=1
        if event.key == pygame.K_w:
            y1-=1
        if event.key == pygame.K_s:
            y1+=1

        if event.key == pygame.K_r:
            x1=200
            y1=200
            score=0
            ball2=True


 #=============================================================

    ball1=[x1,y1]
 #=========================xx-yy============================
    xy=sqrt(((int(newX)-int(newX1))**2)+((int(newY)-int(newY1))**2))
    xc=sqrt(((x1-int(newX1))**2)+((y1-int(newY1))**2))
    cy=sqrt(((int(newX)-x1)**2)+((int(newY)-y1)**2))
    cosA=(((xy**2)+(xc**2))-(cy**2))/(2*xy*xc)

    xd=xc*cosA
    dc=sqrt((xc**2)-(xd**2))


    xx=x1+(dc-7)*math.cos(ygolglob+0.785)
    yy=y1+(dc-7)*math.sin(ygolglob+0.785)



    pygame.draw.line(screen,BLUE,[x1,y1],[int(xx),int(yy)], 1)
 #===========================xx1-yy1==============================
    xy1=sqrt(((int(newX1)-int(newX2))**2)+((int(newY1)-int(newY2))**2))
    xc1=sqrt(((x1-int(newX2))**2)+((y1-int(newY2))**2))
    cy1=sqrt(((int(newX1)-x1)**2)+((int(newY1)-y1)**2))
    cosA=(((xy1**2)+(xc1**2))-(cy1**2))/(2*xy1*xc1)

    xd1=xc1*cosA
    dc1=sqrt((xc1**2)-(xd1**2))


    xx1=x1+(dc1-7)*math.cos(ygolglob+2.355)
    yy1=y1+(dc1-7)*math.sin(ygolglob+2.355)

    #pygame.draw.line(screen,BLUE,[x1,y1],[int(xx1),int(yy1)], 1)

 #===============================xx2-yy2=========================
    xy2=sqrt(((int(newX2)-int(newX3))**2)+((int(newY2)-int(newY3))**2))
    xc2=sqrt(((x1-int(newX3))**2)+((y1-int(newY3))**2))
    cy2=sqrt(((int(newX2)-x1)**2)+((int(newY2)-y1)**2))
    cosA=(((xy2**2)+(xc2**2))-(cy2**2))/(2*xy2*xc2)

    xd2=xc2*cosA
    dc2=sqrt((xc2**2)-(xd2**2))


    xx2=x1+(dc2-7)*math.cos(ygolglob+3.925)
    yy2=y1+(dc2-7)*math.sin(ygolglob+3.925)

    #pygame.draw.line(screen,BLUE,[x1,y1],[int(xx2),int(yy2)], 1)
 #===========================xx3-yy3==============================
    xy3=sqrt(((int(newX3)-int(newX))**2)+((int(newY3)-int(newY))**2))
    xc3=sqrt(((x1-int(newX))**2)+((y1-int(newY))**2))
    cy3=sqrt(((int(newX3)-x1)**2)+((int(newY3)-y1)**2))
    cosA=(((xy3**2)+(xc3**2))-(cy3**2))/(2*xy3*xc3)

    xd3=xc3*cosA
    dc3=sqrt((xc3**2)-(xd3**2))


    xx3=x1+(dc3-7)*math.cos(ygolglob+5.495)
    yy3=y1+(dc3-7)*math.sin(ygolglob+5.495)

    #pygame.draw.line(screen,BLUE,[x1,y1],[int(xx3),int(yy3)], 1)
 #========================================================================


 #===============================логика шара===============================

    bx=1
    by=1



    if ball2==True:
        y1+=bx

        if ball1==[math.ceil(xx1),math.floor(yy1)]:
            ball2=False
            ball3=True

    #elif ball1==[math.floor(xx3),math.ceil(yy3)] and ball3==False and ball4==False and ball5==False:




    elif ball3==True:
        x1+=bx
        if ball1==[int(xx),int(yy)]:
            ball3=False
            ball4=True


    elif ball4==True:
        y1-=bx
        if ball1==[math.floor(xx3),math.ceil(yy3)]:
            ball4=False
            ball5=True



    elif ball5==True:
        x1-=bx
        if ball1==[int(xx2),int(yy2)]:
            ball5=False
            ball2=True


   #========================
    if ball1==[math.floor(xx3),math.ceil(yy3)] and ball2==False and ball3==True and ball4==False and ball5==False:
        ball2=True
        ball3=False

    if ball1==[int(xx),int(yy)] and ball2==True and ball3==False and ball4==False and ball5==False:
        ball5=True
        ball2=False

    if ball1==[math.ceil(xx1),math.floor(yy1)] and ball2==False and ball3==False and ball4==False and ball5==True:
        ball4=True
        ball5=False

    if ball1==[int(xx2),int(yy2)] and ball2==False and ball3==False and ball4==True and ball5==False:
        ball3=True
        ball4=False







 #=========================Fruit=============================================


    pygame.draw.circle(screen,BLUE,[xf,yf],7)
    bf=sqrt(((int(x1)-int(xf))**2)+((int(y1)-int(yf))**2))
    if bf<15:
        score+=10
        xf=random.randint(230,370)
        yf=random.randint(230,370)

 #=========================================================================
    #angle+=0.03


    # background image.
    FPS=250
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
input("Tap exit")