import pygame
import time
import random
import math 

pygame.init()
pygame.mixer.init()

screensize = []
screensize = pygame.display.get_desktop_sizes()
pygame.display.set_caption("honganhcute")
#pygame.display.set_icon(pygame.image.load('E:\Code\Python\Thonny\head.png'))
tanker = []
tanker.append(pygame.image.load("tanker.png"))
tanker.append(pygame.image.load("tanker2.png"))
wx = []
wx.append(pygame.image.load("awin.png"))
wx.append(pygame.image.load("Bwin.png"))

gunsound = pygame.mixer.Sound("fd.mp3")
xc = []
xc.append(pygame.mixer.Sound("loser.mp3"))
xc.append(pygame.mixer.Sound("loser.mp3"))

background = pygame.image.load("background.png")

font = pygame.font.Font('freesansbold.ttf', 32)

n = 700
m = 900
typee = [2,0]
score1 = 0
score2 = 0
s = ""
dx = [0,-1,0,1]
dy = [-1,0,1,0]
xx = []
xxx = []

inside = [41,131,460,830]

sizx = (460 - 40) // 10 + 1
sizy = (830 - 130) // 10 + 1

x = [sizx - 3,3]
y = [sizy - 3,3]

tx = [[[0,0],[0,-1],[-1,0],[-1,1],[1,0],[1,1]],[[0,0],[-1,0],[0,-1],[1,-1],[0,1],[1,1]],[[0,0],[0,1],[-1,0],[1,0],[-1,-1],[1,-1]],[[0,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1]]]
color = ["Black","Red"]

def renderx (x,y,s) : 
    pygame.draw.rect(screen,s,(((x + sizx * 2) % sizx) * 10 + 41,((y + sizy * 2) % sizy) * 10 + 131,10,10))

def inside (x,y) : 
    if x < 0 or x > sizx or y < 0 or y > sizy : 
        return 0
    return 1

def win (i) : 
    screen.blit(wx[i],(0,0))
    xc[i].play()
    pygame.display.update()
    time.sleep(5)
    x[0] = sizx - 3
    x[1] = 3
    y[0] = sizy - 3
    y[1] = 3
    typee[0] = 0
    typee[1] = 0

    xx.clear()
    xxx.clear()

    return i
        

screen = pygame.display.set_mode([n,m])

def update () :

    
    # background

    screen.fill("white")
    screen.blit(background,(0,0))

    pygame.draw.rect(screen,'Black',(36,126,465 - 36 + 1,835 - 126 + 1))
    pygame.draw.rect(screen,'White',(40,130,460 - 40 + 1,830 - 130 + 1))

    text = font.render(s, True, "white", "Black")
    screen.blit(text, (535,208))

    #render tanker 

    for i in range(0,2) : 
       x[i] = (x[i] + dx[typee[i]] + sizx * 2) % sizx
       y[i] = (y[i] + dy[typee[i]] + sizy * 2) % sizy
    # for i in range(0,2) : 
    #    for j in range (0,6) : 
    #         if inside(x[i] + tx[typee[i]][j][0],y[i] + tx[typee[i]][j][1]) == 0 : 
    #             return win (1 - i) 
    for i in range(0,2) : 
        for j in range (0,6) : 
            renderx(x[i] + tx[typee[i]][j][0],y[i] + tx[typee[i]][j][1],color[i])
    for i in range(0,2) : 
       for j in range (0,6) : 
            if (x[1 - i] + dx[typee[1 - i]] ) % sizx == (x[i] + tx[typee[i]][j][0]) % sizx and (y[1 - i] + dy[typee[1 - i]] ) % sizy == (y[i] + tx[typee[i]][j][1]) % sizy : 
               return win(i)
    
    #render bullet 

    for i in range (0,len(xx)) : 
        xx.append([x[0],y[0],typee[0],0])

        xx[i][0] = (xx[i][0] + dx[xx[i][2]] * 2)
        xx[i][1] = (xx[i][1] + dy[xx[i][2]] * 2)

        if inside (xx[i][0],xx[i][1]) : 
            renderx(xx[i][0],xx[i][1],color[xx[i][3]])
            
            
            for j in range (0,6) : 
                if x[1 - xx[i][3]] + tx[typee[1 - xx[i][3]]][j][0] == xx[i][0] and y[1 - xx[i][3]] + tx[typee[1 - xx[i][3]]][j][1] == xx[i][1] : 
                    return win(i)
            
            xxx.append(xx[i])
        else :
            continue

    xx.clear()

    for i in xxx : 
        xx.append(i)
    
    xxx.clear()

    pygame.display.update()
    time.sleep(0.1)

    return 2

running = 1 

while running: 

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            running = 0
        # if event.type == pygame.K_ESCAPE : 
        #     running = False
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_ESCAPE :
                running = 0
            if event.key == pygame.K_LEFT: 
                typee[0] = 1
            elif event.key == pygame.K_RIGHT : 
                typee[0] = 3
            elif event.key == pygame.K_UP :
                typee[0] = 0
            elif event.key == pygame.K_DOWN :
                typee[0] = 2
            elif event.key == pygame.K_p :
                xx.append([x[0],y[0],typee[0],0])
                gunsound.play()
            elif event.key == pygame.K_w : 
                typee[1] = 0
            elif event.key == pygame.K_a : 
                typee[1] = 1
            elif event.key == pygame.K_s : 
                typee[1] = 2
            elif event.key == pygame.K_d : 
                typee[1] = 3
            elif event.key == pygame.K_t : 
                gunsound.play()
                xx.append([x[1],y[1],typee[1],1])

    
    s = str(score1) + "-" + str(score2)

    xxw = update()

    if xxw == 0 : 
        score1 += 1
    elif xxw == 1 : 
        score2 += 1
    print(s,score1,score2)
    

pygame.quit()