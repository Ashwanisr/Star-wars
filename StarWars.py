import pygame
from random import randint
import math
from pygame import mixer

#initalize the pygame module
pygame.init()

#set icon of window  (*Doesn't work on ubuntu )
icon=pygame.image.load('aaa.png')
pygame.display.set_icon(icon)

#set screen size
screen = pygame.display.set_mode((800,600))          #width and height inside the parantheses

#set title of window
pygame.display.set_caption("Star Wars")

#to set an image on the screen
player = pygame.image.load('spaceship.png')
enemy = pygame.image.load("invader.png")
background = pygame.image.load("bacck.jpg")
bullet = pygame.image.load("bullet.png")

#background music
#mixer.music.load('background.wav')
#mixer.music.play(-1)
ss=mixer.Sound("background.wav")
ss.play(-1)

#creating list to fire multiple bullet at a time same can be done with enemy
bullet_state = []
for zz in range(100):
    bullet_state.append("ready")
bullet_no=0

#to store the current score
score = 0

font = pygame.font.Font("freesansbold.ttf",32)
fonta = pygame.font.Font("freesansbold.ttf",64)
testX=10
testY=10

def play(x,y):
    # blit basically draws the image on the screen 
    screen.blit(player,(x,y))

def enemy_dis(x,y):
    screen.blit(enemy,(x,y))

def bullet_dis(x,y,n):
    global bullet_state
    bullet_state[n] = "fire"
    screen.blit(bullet, (x,y))

def is_collison(x,y,a,b):
    dis= math.sqrt(pow(x-a,2)+pow(y-b,2))
    if(dis<27):
        return True
    return False

def show_score(x,y):
    FONT = font.render("Score : "+str(score),True,(0,0,0))
    screen.blit(FONT,(x,y))

def game_end(x,y):
    FONT = font.render("GAME OVER",True,(100,100,255))
    Font = font.render("SCORE: "+str(score),True,(100,100,255))
    screen.blit(FONT,(300,300))
    screen.blit(Font,(300,350))

#screen exits immediately as time taken to run above program is very small
#to delay the window add some kind of loop

#this will delay the screen for some time  (remove comments to see the effect)
#for i in range(10000000):
#    continue
#while running loop is added to do the same work. It delays until we choose cross button

#all event in python are recorded by pygame.event.get()
#if we click the cross button then it is equivalent to QUIT in pygame

#we just take a variable running and that will turn false when we click on cross button
running = True 

spaceX=200
spaceY=500

enemyX= randint(0,768)
enemyY = randint(0,150)

bulletX = []
bulletY = []

for zz in range(100):
    bulletX.append(0)
    bulletY.append(500)

Xchange=0
Ychange=0

enemyXchange=-4
enemyYchange= 30

bulletXchange = 0
bulletYchange = 5

while running:
    #to change the background color of window (rgb)
    screen.fill((255,255,255))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Xchange= -2
            if event.key == pygame.K_RIGHT:
                Xchange = 2
            if event.key == pygame.K_SPACE:
                if(bullet_state[bullet_no] == "ready"):
                    #bullet_sound = mixer.Sound('laser.wav')
                    #bullet_sound.play()
                    mixer.music.load('laser.wav')
                    mixer.music.play()
                    bulletX[bullet_no] = spaceX
                    bullet_dis(bulletX[bullet_no],bulletY[bullet_no],bullet_no)
                    bullet_no = bullet_no + 1
                    if(bullet_no>=10):
                        bullet_no = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange = 0
#working of loop
#the while loop continues to run at fast rate. When I press left key then spaceX becomes -0.3 and next if conditions
#are false so changes spaceX and displays. Loop isn't stucked at that if condition it goes on working and as soon as you 
#lift the key change becomes 0 and again this loop keeps on continuing
#if i add condition play(spaceX+Xchange,spaceY) instead putting at last it will move once for each stroke as the condition
#will be true only once irrespective of time left key is pressed where as putting at end will keep changing as 
#Xchange is -0.3 and it goes to 0 when key is lifted

    spaceX += Xchange

    #adding boundary
    spaceX=max(spaceX,0)
    spaceX=min(spaceX,768)   #image width is 32 pixel so 800-32
    spaceY=max(spaceY,0)
    spaceY=min(spaceY,568)

    enemyX += enemyXchange
    if(enemyX <= 0):
        enemyX = 0
        enemyXchange = 4
        enemyY += enemyYchange
    if(enemyX >=768):
        enemyX =768
        enemyXchange = -4
        enemyY += enemyYchange
    for zz in range(10):
        if(bullet_state[zz]=="fire"):
            if(bulletY[zz] <= 0):
                bulletY[zz] = 500
                bullet_state[zz] = "ready"
                continue
            bulletY[zz] -= bulletYchange
            bullet_dis(bulletX[zz],bulletY[zz],zz)
            if((is_collison(bulletX[zz],bulletY[zz],enemyX,enemyY))):
                #exp_sound = mixer.Sound("explosion.wav")
                #exp_sound.play()
                pygame.mixer.music.load("explosion.wav")
                pygame.mixer.music.play()
                enemyX = randint(0,767)
                enemyY = randint(0,150)
                bullet_state[zz] = "ready"
                bulletY[zz] = 500
                score = score + 1

    #shows the player image (always put after background bcz background will be painted first then player)
    play(spaceX,spaceY)
    enemy_dis(enemyX,enemyY)

    if(enemyY >= 468):
        break
    show_score(0,540)

    #to update window after each event
    pygame.display.update()

run=True
while run:
    screen.fill((255,255,255))
    game_end(0,0)
    for event in pygame.event.get():
        if(event.type== pygame.QUIT):
            run=False
    pygame.display.update()