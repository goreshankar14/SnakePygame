import pygame
import sys
import time
import random
SH = 320
SW = 480
win = pygame.display.set_mode((SW, SH))
icon = pygame.image.load("gameicon.png")
pygame.display.set_icon(icon)
ground=pygame.image.load("snakeGround.png")
scr=pygame.image.load("startScreen.png")
pygame.display.set_caption(" Hisssss ")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
green = (0,200,0)
def welcome():
    win.fill(white)
    win.blit(scr, (0, 0))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    
    return

def gameOver(score):
    win.fill(white)
    win.blit(ground,(0,0))
    s1 = pygame.Surface((25,320))
    s2 = pygame.Surface((480,25))
    s3 = pygame.Surface((480,320))
    s4 = pygame.Surface((480,295))
    s1.fill(green)
    s2.fill(green)
    s3.fill(green)
    s4.fill(green)
    win.blit(s1, (0,0))
    win.blit(s2, (0,0))
    win.blit(s3, (0,295))
    win.blit(s4, (455,25))

    text=font.render(" Game Over ",True,black)
    win.blit(text,(170,110))

    scor=font.render(" Score : "+str(score),True,black)
    win.blit(scor,(3,3))

    cont=font.render(" Press Space To Continue ",True,black)
    win.blit(cont,(110,150))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        startGame(200,200)

    pygame.display.update()

def displayScreen(score):
    stri=" Score : "+str(score)
    ons=font.render(stri,True,black)
    win.blit(ons,(3,3))

def plot_snake(win,color,snk_list,snk_width,snk_height):
    for x,y in snk_list:
        pygame.draw.rect(win,color,(x,y,snk_width,snk_height))

def startGame(x,y):
    playing=True
    snk_width=10
    snk_height=10
    x_v=0
    y_v=0
    f_x=random.randint(30,SW-snk_width-35)
    f_y=random.randint(30,SH-snk_height-35)
    score=0
    collide=False
    snk_list=[]
    snk_length=1

    while playing:

        win.fill(white)
        win.blit(ground,(0,0))

        s1 = pygame.Surface((25,320))
        s2 = pygame.Surface((480,25))
        s3 = pygame.Surface((480,320))
        s4 = pygame.Surface((480,295))
        s1.fill(green)
        s2.fill(green)
        s3.fill(green)
        s4.fill(green)
        win.blit(s1, (0,0))
        win.blit(s2, (0,0))
        win.blit(s3, (0,295))
        win.blit(s4, (455,25))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                playing=False

        if collide:
            gameOver(score)

        else:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y_v=-3
                x_v=0
            elif keys[pygame.K_DOWN]:
                y_v=3
                x_v=0
            elif keys[pygame.K_LEFT]:
                y_v=0
                x_v=-3
            elif keys[pygame.K_RIGHT]:
                y_v=0
                x_v=3

            if ( x > x_v or x < (SW-snk_width-x_v)) or ( y > y_v or y < (SH-snk_height-y_v)):
                x=x+x_v
                y=y+y_v
            else:
                x=x+1
                y=y+1

            if abs(x-f_x)<10 and abs(y-f_y)<10:
                score+=10
                f_x=random.randint(30,SW-snk_width-35)
                f_y=random.randint(30,SH-snk_height-35)
                snk_length+=6

            displayScreen(score)

            if ( x < 25 or x > (SW-snk_width-28)) or ( y < 25 or y > (SH-snk_height-28)):
                collide=True

            snk_head = []
            snk_head.append(x)
            snk_head.append(y)
            snk_list.append(snk_head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snk_head in snk_list[:-1]:
                collide = True

            plot_snake(win,white,snk_list,snk_width,snk_height)
            pygame.draw.rect(win,red,(f_x,f_y,snk_width,snk_height))

            pygame.display.update()
            clock.tick(30)

    pygame.quit()
    sys.exit(0)



if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    welcome()
    startGame(200,200)
    
